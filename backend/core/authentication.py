import datetime

import jwt
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from .models import User


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_data = get_authorization_header(request).split()

        if auth_data and len(auth_data) == 2:
            access_token = auth_data[1].decode("utf-8")
        else:
            access_token = request.COOKIES.get("access_token")

        if access_token:
            user = User.objects.get(pk=decode_access_token(access_token))
            return (user, auth_data)

        raise exceptions.AuthenticationFailed("Invalid token")


def create_access_token(id):
    return jwt.encode(
        {
            "user_id": id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
            "iat": datetime.datetime.utcnow(),
        },
        "access_secret",
        algorithm="HS256",
    )


def decode_access_token(token):
    try:
        payload = jwt.decode(token, "access_secret", algorithms=["HS256"])
        return payload["user_id"]
    except:  # noqa: E722
        raise exceptions.AuthenticationFailed("Unauthenticated")


def create_refresh_token(id):
    return jwt.encode(
        {
            "user_id": id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
            "iat": datetime.datetime.utcnow(),
        },
        "refresh_secret",
        algorithm="HS256",
    )


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, "refresh_secret", algorithms=["HS256"])
        return payload["user_id"]
    except:  # noqa: E722
        raise exceptions.AuthenticationFailed("Unauthenticated")
