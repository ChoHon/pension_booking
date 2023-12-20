from django.db import models
from util.base_models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Pension(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'pension'