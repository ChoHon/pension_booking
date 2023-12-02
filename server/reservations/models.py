from django.db import models

class Reservation(models.Model):
    room = models.ForeignKey('rooms.room', on_delete=models.CASCADE)
    option_bbq = models.BooleanField()
    option_is_over_capacity = models.BooleanField()
    discount = models.IntegerField()
    end_price = models.IntegerField()

    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *arg, **kwargs):
    #     self.end_price = 

    class Meta:
        db_table = 'reservation'