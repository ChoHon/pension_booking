from django.db import models
from django.utils import timezone

class User(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)