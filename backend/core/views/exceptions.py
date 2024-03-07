from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import exceptions


def validate_email__exception(email):
    try:
        validate_email(email)
    except ValidationError:
        raise exceptions.AuthenticationFailed(
            "Please provide a valid email address."
        )

def missing_data__exception(email, password):
    if not email or not password:
        raise exceptions.AuthenticationFailed(
            "Please provide both email and password to login."
        )

def user_exists__exception(User, email, username):
    if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            raise exceptions.AuthenticationFailed(
                "A user with that email or username already exists."
            )

def invalid_credentials__exception(user, password):
    if user and user.check_password(password):
            return None

    raise exceptions.AuthenticationFailed(
        "Sorry, we could not find a user with the provided credentials."
    )

def not_logged_in__exception(refesh_token):
    if not refesh_token:
        raise exceptions.AuthenticationFailed(
            "Please login to continue."
        )

def invalid_token__exception(user, token):
    if not PasswordResetTokenGenerator().check_token(user, token):
            raise exceptions.AuthenticationFailed(
                "The token provided is invalid. Please request a new one."
            )

def invalid_email__exception(user):
    if not user:
        raise exceptions.AuthenticationFailed(
            "Sorry, we could not find a user with the provided email. Please try again."
        )