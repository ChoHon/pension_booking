from django.db import models
from util.base_models import BaseModel


class Reservation(BaseModel):
    room = models.ForeignKey('rooms.room', on_delete=models.CASCADE)
    option_bbq = models.BooleanField()
    option_over_capacity = models.BooleanField()
    discount = models.IntegerField()
    final_payment = models.IntegerField()

    is_canceled = models.BooleanField(default=False)

    # def save(self, *arg, **kwargs):
    #     self.end_price = 

    class Meta:
        db_table = 'reservation'