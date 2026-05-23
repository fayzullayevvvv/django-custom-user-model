from rest_framework import serializers

from .models import User, Todo


class UserSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.