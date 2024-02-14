from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from .authentication import JWTAuthentication, create_access_token, create_refresh_token
from .models import User
from .serializers import UserSerializer


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        data = request.data

        if data["password"] != data["password_confirm"]:
            raise exceptions.APIException("Passwords do not match!")

        serializer = UserSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        data = request.data

        email = data["email"]
        password = data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid credentials")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Invalid credentials")

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()

        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        response.data = {"token": access_token}

        return response


class UserView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response(UserSerializer(request.user).data)
