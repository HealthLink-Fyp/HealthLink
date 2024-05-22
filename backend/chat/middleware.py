# middleware.py
from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
from urllib.parse import parse_qs
from core.authentication import JWTAuthentication
from django.http import HttpRequest
from healthlink.utils.exceptions import InvalidToken, TokenExpired


class JwtAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        self.inner = inner

    @database_sync_to_async
    def get_user(self, jwt_token):
        request = HttpRequest()
        request.META["HTTP_AUTHORIZATION"] = f"Bearer {jwt_token}"
        try:
            user, auth_data = JWTAuthentication().authenticate(request)
        except TokenExpired or InvalidToken:
            user = None
        return user

    async def __call__(self, scope, receive, send):
        query_string = parse_qs(scope["query_string"].decode())
        jwt_token = query_string.get("token")
        if jwt_token:
            scope["user"] = await self.get_user(jwt_token[0])
        else:
            scope["user"] = None

        return await super().__call__(scope, receive, send)
