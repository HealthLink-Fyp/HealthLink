# Django Imports
# from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.utils import timezone

# Rest Framework Imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.authentication import (
    JWTAuthentication,
    create_access_token,
    create_refresh_token,
    decode_refresh_token,
)

# Local Imports
from core.models import User, UserForgot, UserToken
from core.serializers import UserSerializer

# Third Part Imports
# from core.tasks import send_mail_task

from django.core.validators import validate_email

from rest_framework.exceptions import (
    AuthenticationFailed,
    NotFound,
    PermissionDenied,
    NotAuthenticated,
    ValidationError,
)


class RegisterView(APIView):
    def post(self, request):
        """
        Register the user
        """
        # Check if the user is an admin
        if request.data.get("role") == "admin":
            raise PermissionDenied("Not allowed.")

        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        """
        Login the user
        """
        email = request.data.get("email", "").strip().lower()
        password = request.data.get("password", "")

        # Check if the email is valid
        try:
            validate_email(email)
        except Exception:
            raise ValidationError("Invalid email.")

        user = User.objects.filter(email=email).first()

        # Check if the user exists
        if not user:
            raise NotFound("User not found.")

        # Check if the user is an admin
        if user.role == "admin":
            raise PermissionDenied("Not allowed.")

        # Check if the password is correct
        if not user.check_password(password):
            raise AuthenticationFailed("Invalid credentials.")

        access_token = create_access_token(user=user)
        refresh_token = create_refresh_token(user=user)
        UserToken.objects.create(
            user=user,
            token=refresh_token,
            expire_at=timezone.now() + timezone.timedelta(days=7),
        )

        response = Response()
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        response.data = {"access_token": access_token, "refresh_token": refresh_token}
        response.status_code = status.HTTP_200_OK
        return response


class UserView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        """
        Get the user's information
        """
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)


class RefreshView(APIView):
    def post(self, request):
        """
        Refresh the access token
        """

        refresh_token = request.COOKIES.get("refresh_token", False)

        # Check if the refresh token is valid
        if not refresh_token:
            raise NotAuthenticated("Not authenticated.")

        user_id = decode_refresh_token(token=refresh_token)
        user = User.objects.filter(id=user_id).first()

        # Check if the user exists
        if not user:
            raise NotFound("User not found.")

        filter_params = {
            "user": user,
            "token": refresh_token,
            "expire_at__gt": timezone.now(),
        }

        # Check if the user is logged in
        if not refresh_token or not user_id or not user:
            raise NotAuthenticated("Not authenticated.")

        # Check if the refresh token is valid
        if not UserToken.objects.filter(**filter_params).exists():
            raise AuthenticationFailed("Invalid refresh token.")

        access_token = create_access_token(user=user)
        return Response({"access_token": access_token}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        """
        Logout the user
        """
        refresh_token = request.COOKIES.get("refresh_token", False)

        # Check if the user is logged in
        if not refresh_token:
            raise NotAuthenticated("Not authenticated.")

        UserToken.objects.filter(token=refresh_token).delete()

        response = Response()
        response.delete_cookie(key="refresh_token")
        response.data = {"message": "Success"}
        response.status_code = status.HTTP_200_OK
        return response


class ForgotView(APIView):
    def post(self, request):
        """
        Send an email to the user to reset their password
        """
        email = request.data["email"].strip().lower()

        user = User.objects.filter(email=email).first()

        # Check if the user exists
        if not user:
            raise NotFound("User not found.")

        token = PasswordResetTokenGenerator().make_token(user)
        UserForgot.objects.create(user=user, email=email, token=token)

        # forgot_url = settings.FRONTEND_URL + "/" + token
        # message = f"Dear {user.first_name},\n\nTo select a new password, click on the below link:\n\n\n\n{forgot_url}"
        # send_mail_task.delay(email=email, message=message)

        return Response(
            {
                "message": f"Check your email: {email} to reset your password. Token: {token}"
            },
            status=status.HTTP_200_OK,
        )


class ResetView(APIView):
    def post(self, request):
        """
        Reset the user's password
        """
        token = request.data.get("token")
        password = request.data.get("password")

        # Check for password strength
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        user_reset = UserForgot.objects.filter(token=token).first()

        # Check if the token is valid
        if not user_reset:
            raise NotFound("Invalid token.")

        user = User.objects.filter(email=user_reset.email).first()

        # Check if the user exists
        if not user:
            raise NotFound("User not found.")

        user.set_password(password)
        user.save()

        return Response({"message": "Success"}, status=status.HTTP_200_OK)
