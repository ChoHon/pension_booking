from django.db import models
from util.base_models import BaseModel


class Reservation(BaseModel):
    room = models.ForeignKey('rooms.room', on_delete=models.CASCADE)
    reservation_date = models.DateField()

    option_bbq = models.BooleanField()
    option_over_capacity = models.BooleanField()

    discount = models.IntegerField()
    final_payment = models.IntegerField()

    is_canceled = models.BooleanField(default=False)

    class Meta:
        db_table = 'reservation'