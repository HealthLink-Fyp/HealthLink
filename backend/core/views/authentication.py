# Django Imports
# from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.utils import timezone

# Rest Framework Imports
from rest_framework import exceptions, status
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

from .exceptions import (
    missing_data_exception,
    validate_email_exception,
    user_exists_exception,
    invalid_credentials_exception,
    invalid_token_exception,
    not_logged_in_exception,
    user_not_found_exception
)


class RegisterView(APIView):
    def post(self, request):

        email = request.data.get("email", False)
        password = request.data.get("password", False)
        username = request.data.get("username", False)
        email = email.strip().lower()

        missing_data_exception(email, password)
        validate_email_exception(email)
        user_exists_exception(User, email, username)

        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):

        email = request.data.get("email", "")
        password = request.data.get("password", "")

        email = email.strip().lower()
        

        missing_data_exception(email, password)
        validate_email_exception(email)

        user = User.objects.filter(email=email).first()
        invalid_credentials_exception(user, password)

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)
        UserToken.objects.create(
            user_id=user.id,
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
        return Response(
            UserSerializer(request.user).data,
            status=status.HTTP_200_OK,
        )


class RefreshView(APIView):
    def post(self, request):

        refresh_token = request.COOKIES.get("refresh_token")
        id = decode_refresh_token(token=refresh_token)

        filter_params = {'user_id': id, 'token': refresh_token, 'expire_at__gt': timezone.now()}

        if not UserToken.objects.filter(**filter_params).exists():
            raise exceptions.AuthenticationFailed("Unauthenticated")

        access_token = create_access_token(id=id)
        return Response({"access_token": access_token}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):

        refesh_token = request.COOKIES.get("refresh_token", False)
        not_logged_in_exception(refesh_token)

        UserToken.objects.filter(token=refesh_token).delete()
        response = Response()

        response.delete_cookie(key="refresh_token")
        response.data = {"message": "Success"}
        response.status_code = status.HTTP_200_OK

        return response


class ForgotView(APIView):
    def post(self, request):

        email = request.data["email"]
        validate_email_exception(email)

        user = User.objects.filter(email=email).first()
        user_not_found_exception(user)

        token = PasswordResetTokenGenerator().make_token(user)
        UserForgot.objects.create(email=email, token=token)

        # forgot_url = settings.FRONTEND_URL + "/" + token
        # message = f"Dear {user.first_name},\n\nTo select a new password, click on the below link:\n\n\n\n{forgot_url}"
        # send_mail_task.delay(email=email, message=message)

        return Response(
            {"message": f"Check your email: {email} to reset your password"},
            status=status.HTTP_200_OK,
        )


class ResetView(APIView):
    def post(self, request):

        token = request.data.get("token")
        password = request.data.get("password")

        user_reset = UserForgot.objects.filter(token=token).first()
        user = User.objects.filter(email=user_reset.email).first()

        invalid_token_exception(user, token)
        user_not_found_exception(user)

        user.set_password(password)
        user.save()

        return Response({"message": "Success"}, status=status.HTTP_200_OK)