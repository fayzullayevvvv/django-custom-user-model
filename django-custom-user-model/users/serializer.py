from rest_framework import serializers

from .models import User, Todo


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_verified",
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }
        read_only_fields = ["id"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = [
            "id",
            "title",
            "description",
            "is_completed",
            "user",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "created_at",
            "updated_at",
        ]

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Title kamida 3 ta belgidan iborat bo'lishi kerak"
            )
        
        return value