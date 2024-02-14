import secrets

from django.core.mail import send_mail
from django.utils import timezone
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from .authentication import (
    JWTAuthentication,
    create_access_token,
    create_refresh_token,
    decode_refrsh_token,
)
from .models import User, UserForgot, UserToken
from .serializers import UserSerializer


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        data = request.data

        if data["password"] != data["password_confirm"]:
            raise exceptions.APIException("Passwords do not match!")

        serializer = UserSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        data = request.data

        email = data["email"]
        password = data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid credentials")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Invalid credentials")

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        UserToken.objects.create(
            user_id=user.id,
            token=refresh_token,
            expire_at=timezone.now() + timezone.timedelta(days=7),
        )

        response = Response()
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        response.data = {"token": access_token}

        return response


class UserView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class RefreshView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")
        id = decode_refrsh_token(token=refresh_token)

        if not UserToken.objects.filter(
            user_id=id,
            token=refresh_token,
            expire_at__gt=timezone.now(),
        ).exists():
            raise exceptions.AuthenticationFailed("Unauthenticated")

        access_token = create_access_token(id=id)

        return Response({"access_token": access_token})


class LogoutView(APIView):
    def post(self, request):
        refesh_token = request.COOKIES.get("refesh_token")
        UserToken.objects.filter(token=refesh_token).delete()
        response = Response()
        response.delete_cookie(key="refresh_token")
        response.data = {"message": "Success"}
        return response


class ForgotView(APIView):
    def post(self, request):
        token = secrets.token_hex(15)
        email = request.data["email"]
        UserForgot.objects.create(email=email, token=token)

        if email:
            user = User.objects.filter(email=email).first()

        forgot_url = "https://localhost:3000/reset/" + token

        subject = "Reset your HealthLink Password"
        message = f"Dear {user.first_name}, To select a new password, click on thie below link:\n {forgot_url}"
        send_mail(
            subject=subject,
            message=message,
            from_email=None,
            recipient_list=[email],
            fail_silently=False,
        )

        return Response({"message": "Success"})


class ResetView(APIView):
    def post(self, request):
        data = request.data

        if data["password"] != data["password_confirm"]:
            raise exceptions.APIException("Passwords do not match!")

        reset_password = UserForgot.objects.filter(token=data["token"]).first()

        if not reset_password:
            raise exceptions.APIException("Inalid Link!")

        user = User.objects.filter(email=reset_password.email).first()

        if not user:
            raise exceptions.APIException("User not found!")

        user.set_password(data["password"])
        user.save()

        return Response({"message": "Success"})
