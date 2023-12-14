from rest_framework import serializers
from pensions.models import Pension

class PensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pension
        fields = '__all__'