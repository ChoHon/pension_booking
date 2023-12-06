from django.db import models
from util.base_models import BaseModel

class Room(BaseModel):
    pension = models.ForeignKey('pensions.Pension', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    capacity = models.IntegerField()
    price_peak_season = models.IntegerField(default=0)
    price_off_season = models.IntegerField(default=0)

    class Meta:
        db_table = 'room'