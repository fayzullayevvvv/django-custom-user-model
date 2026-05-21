from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserCreateSerializer, UserSerializer

User = get_user_model()


class UserCreateAPIView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            existing_user = User.objects.filter(username=serializer.validated_data['username']).first()
            if existing_user:
                return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data.get('email'),
                password=serializer.validated_data['password']
            )
            result = UserSerializer(user).data
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request) -> Response:
        return Response({"message": "GET method is not allowed for this endpoint"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    