from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Pension(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pension_name = models.CharField(max_length=30)
    pension_address = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Room(models.Model):
    pension = models.ForeignKey(Pension, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=10)
    room_capacity = models.IntegerField(null=True)
    room_price = models.IntegerField(null=False, blank=False)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)