import secrets

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.utils import timezone
from rest_framework import exceptions, status
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
        email = request.data.get("email", False)
        password = request.data.get("password", False)

        if not email or not password:
            return Response(
                {"error", "Both email and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        email = email.strip().lower()

        try:
            validate_email(email)
        except ValidationError:
            return Response(
                {"error", "Please provide a valid email address"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error", "User with this email already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email", False)
        password = request.data.get("password", False)

        # Raise exception if any of the above are missing
        if not email or not password:
            return Response(
                {"error", "Both email and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate email
        email = email.strip().lower()
        try:
            validate_email(email)
        except ValidationError:
            return Response(
                {"error", "Please provide a valid email address"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Get the user
        user = User.objects.filter(email=email).first()

        if user:
            if not user.check_password(password):
                return Response(
                    {
                        "error": "Sorry, we could not find a user with the provided credentials. Please try again.",
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )
        else:
            access_token = create_access_token(user.id)
            refresh_token = create_refresh_token(user.id)
            UserToken.objects.create(
                user_id=user.id,
                token=refresh_token,
                expire_at=timezone.now() + timezone.timedelta(days=7),
            )

        response = Response()
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        response.data = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        response.status_code = status.HTTP_200_OK

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
        refesh_token = request.COOKIES.get("refesh_token", False)

        if not refesh_token:
            return Response(
                {"error": "You are not Logged In."}, status=status.HTTP_400_BAD_REQUEST
            )
        UserToken.objects.filter(token=refesh_token).delete()
        response = Response()
        response.delete_cookie(key="refresh_token")
        response.data = {"message": "Success"}
        response.status_code = status.HTTP_200_OK
        return response


class ForgotView(APIView):
    def post(self, request):
        token = secrets.token_hex(15)
        email = request.data["email"]
        UserForgot.objects.create(email=email, token=token)

        if not email:
            return Response(
                {"error", "Your email was incorrect. Please try again."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.filter(email=email).first()

        frontend_url = settings.FRONTEND_URL

        if frontend_url:
            forgot_url = frontend_url + "/" + token
        else:
            forgot_url = "https://localhost:4200/reset/" + token

        subject = "Link to Reset your HealthLink Password"
        message = f"Dear {user.first_name},\n\nTo select a new password, click on the below link:\n\n\n\n{forgot_url}"
        send_mail(
            subject=subject,
            message=message,
            from_email=None,
            recipient_list=[email],
            fail_silently=False,
        )

        return Response({"message": "Success"}, status=status.HTTP_200_OK)


class ResetView(APIView):
    def post(self, request):
        data = request.data

        if data["password"] != data["password_confirm"]:
            raise exceptions.APIException("Passwords do not match!")

        reset_password = UserForgot.objects.filter(token=data["token"]).first()

        if not reset_password:
            return Response(
                {"error", "Your password reset link was incorrect. Please try again."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.filter(email=reset_password.email).first()

        if not user:
            return Response(
                {"error", "Your email was invalid. Please try again."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(data["password"])
        user.save()

        return Response({"message": "Success"}, status=status.HTTP_200_OK)
