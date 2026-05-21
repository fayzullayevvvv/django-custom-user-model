from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status



class UserCreateAPIView(APIView):
    def post(self, request: Request) -> Response:
        # Implement user creation logic here
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        return Response({"message": "GET method is not allowed for this endpoint"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    