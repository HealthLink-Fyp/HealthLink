from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.tokens import PasswordResetTokenGenerator


def validate_email__exception(email):
    try:
        validate_email(email)
    except ValidationError:
        return Response(
            {"error", "Please provide a valid email address"},
            status=status.HTTP_400_BAD_REQUEST,
        )

def missing_data__exception(email, password):
    if not email or not password:
        return Response(
            {"error", "Both email and password are required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

def user_exists__exception(User, email, username):
    if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            return Response(
                {"error", "User already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

def invalid_credentials__exception(user, password):
    if not user.check_password(password):
        return Response(
            {
                "error": "Sorry, we could not find a user with the provided credentials. Please try again.",
            },
            status=status.HTTP_403_FORBIDDEN,
        )

def not_logged_in__exception(refesh_token):
    if not refesh_token:
        return Response(
            {"error": "You are not Logged In."}, status=status.HTTP_400_BAD_REQUEST
        )

def invalid_token__exception(user, token):
    if not PasswordResetTokenGenerator().check_token(user, token):
            return Response(
                {"error", "Token is invalid."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

def invalid_email__exception(user):
    if not user:
        return Response(
            {"error", "Your email was incorrect. Please try again."},
            status=status.HTTP_400_BAD_REQUEST,
        )