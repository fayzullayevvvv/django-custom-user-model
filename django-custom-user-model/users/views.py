from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import UserSerializer, TodoSerializer
from .models import User, Todo


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoListCreateView(APIView):
    def get(self, request, user_id):
        todos = Todo.objects.filter(user=user_id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    def get(self, request, user_id, id):
        try:
            todo = Todo.objects.get(user=user_id, id=id)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id, id):
        try:
            todo = Todo.objects.get(user=user_id, id=id)
        except Todo.DoesNotExist:
            return Response(
                {"message": "Todo not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, id):
        try:
            todo = Todo.objects.get(user=user_id, id=id)
        except Todo.DoesNotExist:
            return Response(
                {"message": "Todo not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        todo.delete()
        return Response(
            {"message": "Todo deleted successfully"},
            status=status.HTTP_200_OK
        )