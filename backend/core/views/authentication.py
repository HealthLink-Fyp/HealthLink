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
from healthlink.utils.exceptions import (
    AlreadyExists,
    NotFound,
    InvalidData,
    InvalidToken,
)

# Third Part Imports
# from core.tasks import send_mail_task


from django.core.validators import validate_email


class RegisterView(APIView):
    def post(self, request):
        email = request.data.get("email", False)
        password = request.data.get("password", False)

        if not email or not password:
            raise NotFound("Email and password")

        email = email.strip().lower()

        # Check if the email is valid
        try:
            validate_email(email)
        except Exception:
            raise InvalidData("Email")

        if User.objects.filter(email=email).exists():
            raise AlreadyExists("User (email)")

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        """
        Login the user
        """
        username = request.data.get("username", "").strip().lower()
        email = request.data.get("email", "").strip().lower()
        password = request.data.get("password", "")

        # Email or username, both can be used to login so at least one should be present
        if not email and not username or not password:
            raise InvalidData("Email or username and password")

        if email:
            # Check if the email is valid
            try:
                validate_email(email)
            except Exception:
                raise InvalidData("Email")

            user = User.objects.filter(email=email).first()
        elif username:
            user = User.objects.filter(username=username).first()

        # Check if the user exists
        if not user:
            raise NotFound("User")

        # Check if the password is correct
        if not user.check_password(password):
            raise InvalidData("Password")

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
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        """
        Update the user's information
        """
        user = request.user
        data = request.data.copy()
        data.pop("email", None)
        data.pop("password", None)
        data.pop("role", None)

        serializer = UserSerializer(user, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        """
        Delete the user
        """
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RefreshView(APIView):
    def post(self, request):
        """
        Refresh the access token
        """

        refresh_token = request.COOKIES.get("refresh_token", False)

        # Check if the refresh token is valid
        if not refresh_token:
            raise InvalidToken()

        user_id = decode_refresh_token(token=refresh_token)
        user = User.objects.filter(id=user_id).first()

        # Check if the user exists
        if not user:
            raise NotFound("User")

        filter_params = {
            "user": user,
            "token": refresh_token,
            "expire_at__gt": timezone.now(),
        }

        # Check if the refresh token is valid
        if not UserToken.objects.filter(**filter_params).exists():
            raise InvalidToken()

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
            raise InvalidToken()

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
            raise NotFound("User")

        token = PasswordResetTokenGenerator().make_token(user)
        UserForgot.objects.create(user=user, email=email, token=token)

        # forgot_url = settings.FRONTEND_URL + "/" + token
        # message = f"Dear {user.first_name},\n\nTo select a new password, click on the below link:\n\n\n\n{forgot_url}"
        # send_mail_task.delay(email=email, message=message)

        response = Response()
        response.data = {"message": "Email sent successfully."}
        response.status_code = status.HTTP_200_OK
        return response


class ResetView(APIView):
    def post(self, request):
        """
        Reset the user's password
        """
        token = request.data.get("token")
        password = request.data.get("password")

        # Check for password strength
        if len(password) < 8:
            raise InvalidData("Password")

        user_reset = UserForgot.objects.filter(token=token).first()

        # Check if the token is valid
        if not user_reset:
            raise InvalidToken()

        user = User.objects.filter(email=user_reset.email).first()

        # Check if the user exists
        if not user:
            raise NotFound("User")

        user.set_password(password)
        user.save()

        response = Response()
        response.data = {"message": "Password reset successfully."}
        response.status_code = status.HTTP_200_OK
        return response
