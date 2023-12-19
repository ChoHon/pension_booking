from os import read
from rest_framework import serializers
from pensions.models import Pension

class RoomListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "id": value.id,
            "name": value.name,
            "capacity": value.capacity,
            "price_peak_season": value.price_peak_season,
            "price_off_season": value.price_off_season,
        }

class PensionSerializer(serializers.ModelSerializer):
    rooms = RoomListingField(many=True, read_only=True)

    class Meta:
        model = Pension
        fields = '__all__'