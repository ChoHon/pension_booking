from django.db import models

class Room(models.Model):
    pension = models.ForeignKey('pensions.Pension', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    capacity = models.IntegerField()
    price_peak_season = models.IntegerField()
    price_off_season = models.IntegerField()
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'room'