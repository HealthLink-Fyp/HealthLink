from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
import re

def missing_data_exception(*args):
    for arg in args:
        if not arg:
            return Response({"detail": f"{arg} is missing."}, status=status.HTTP_400_BAD_REQUEST)

def validate_email_exception(email):
    email = email.lower()
    regular_expression = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"
    if not re.match(regular_expression, email):
        return Response({"detail": "Invalid email."}, status=status.HTTP_400_BAD_REQUEST)
    return email

def invalid_credentials_exception(user, password):
    if not user.check_password(password) or not user:
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

def user_not_found_exception(user):
    if not user:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

def admin_not_allowed_exception(user):
    if user.role == "admin":
        return Response({"detail": "Not allowed."}, status=status.HTTP_403_FORBIDDEN)

def user_exists_exception(User, email, username):
    if User.objects.filter(Q(email=email) | Q(username=username)).exists():
        return Response({"detail": "User already exists."}, status=status.HTTP_400_BAD_REQUEST)

def not_logged_in_exception(refresh_token):
    if not refresh_token:
        return Response({"detail": "Not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

def invalid_token_exception(user, token):
    if not PasswordResetTokenGenerator().check_token(user, token):
        return Response({"detail": "Invalid Token."}, status=status.HTTP_401_UNAUTHORIZED)
