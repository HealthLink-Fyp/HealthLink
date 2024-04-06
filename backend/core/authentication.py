# Django Imports
# Import secret keys from settings.py
from django.conf import settings

# Rest Framework Imports
from rest_framework.exceptions import AuthenticationFailed, NotFound
from rest_framework.authentication import BaseAuthentication, get_authorization_header

# Python Imports
import datetime
import jwt

# Local Imports
from .models import User

# JWT Secret Keys
jwt_refresh_secret = settings.JWT_REFRESH_SECRET
jwt_access_secret = settings.JWT_ACCESS_SECRET

# JWT Expire Time
jwt_access_expire = settings.JWT_ACCESS_EXPIRE
jwt_refresh_expire = settings.JWT_REFRESH_EXPIRE


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_data = get_authorization_header(request).split()

        # Check if the token is provided
        if not auth_data or len(auth_data) == 1:
            raise NotFound("No token provided")

        identifier = auth_data[0].decode("utf-8")
        access_token = auth_data[1].decode("utf-8")

        # Check if the token is valid
        if identifier != "Bearer" or not access_token:
            raise AuthenticationFailed("Invalid token")

        try:
            user = User.objects.get(pk=decode_access_token(access_token))
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")
        return (user, auth_data)


def create_access_token(user):
    return jwt.encode(
        {
            "user_id": user.id,
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(seconds=jwt_access_expire),
            "iat": datetime.datetime.utcnow(),
        },
        key=jwt_access_secret,
        algorithm="HS256",
    )


def decode_access_token(token):
    try:
        payload = jwt.decode(token, key=jwt_access_secret, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Token has expired")
    except (jwt.InvalidTokenError, jwt.DecodeError):
        raise AuthenticationFailed("Invalid token")


def create_refresh_token(user):
    return jwt.encode(
        {
            "user_id": user.id,
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(days=jwt_refresh_expire),
            "iat": datetime.datetime.utcnow(),
        },
        key=jwt_refresh_secret,
        algorithm="HS256",
    )


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, key=jwt_refresh_secret, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Token has expired")
    except (jwt.InvalidTokenError, jwt.DecodeError):
        raise AuthenticationFailed("Invalid token")
