from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class UserView(APIView):
    def post(self, request):
        return Response(request.data)
