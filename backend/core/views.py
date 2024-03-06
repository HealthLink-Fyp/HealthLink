# Django Imports
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils import timezone

# Rest Framework Imports
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .authentication import (
    JWTAuthentication,
    create_access_token,
    create_refresh_token,
    decode_refresh_token,
)

# Local Imports
from .models import User, UserForgot, UserToken
from .serializers import UserSerializer

# Third Part Imports
from .tasks import send_mail_task


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
        else:
            return Response(
                {
                    "error": "Sorry, we could not find a user with the provided credentials. Please try again.",
                },
                status=status.HTTP_403_FORBIDDEN,
            )


class UserView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response(
            UserSerializer(request.user).data,
            status=status.HTTP_200_OK,
        )


class RefreshView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")
        id = decode_refresh_token(token=refresh_token)

        if not UserToken.objects.filter(
            user_id=id,
            token=refresh_token,
            expire_at__gt=timezone.now(),
        ).exists():
            raise exceptions.AuthenticationFailed("Unauthenticated")

        access_token = create_access_token(id=id)

        return Response({"access_token": access_token}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        refesh_token = request.COOKIES.get("refresh_token", False)

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
        email = request.data["email"]

        try:
            validate_email(email)
        except ValidationError:
            return Response(
                {"error", "Please provide a valid email address"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.filter(email=email).first()

        token = PasswordResetTokenGenerator().make_token(user)

        UserForgot.objects.create(email=email, token=token)

        if not user:
            return Response(
                {"error", "Your email was incorrect. Please try again."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        forgot_url = settings.FRONTEND_URL + "/" + token

        message = f"Dear {user.first_name},\n\nTo select a new password, click on the below link:\n\n\n\n{forgot_url}"

        # send_mail_task.delay(email=email, message=message)

        return Response(
            {"message": f"Check your {email} - {message} to reset your password"},
            status=status.HTTP_200_OK,
        )


class ResetView(APIView):
    def post(self, request):
        token = request.data.get("token")
        password = request.data.get("password")

        user_reset = UserForgot.objects.filter(token=token).first()
        user = User.objects.filter(email=user_reset.email).first()

        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response(
                {"error", "Token is invalid."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if not user:
            return Response(
                {"error", "Your email was invalid. Please try again."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(password)
        user.save()

        return Response({"message": "Success"}, status=status.HTTP_200_OK)
