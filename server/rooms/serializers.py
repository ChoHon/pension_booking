from rest_framework import serializers
from rooms.models import Room
from pensions.serializers import PensionSerializer

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response["pension"] = PensionSerializer(instance.pension).data
    #     return response