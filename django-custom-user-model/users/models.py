from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    is_verified = models.BooleanField(default=False)


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
