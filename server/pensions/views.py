from rest_framework import status, viewsets
from rest_framework.response import Response
from pensions.models import Pension
from pensions.serializers import PensionSerializer

class PensionViewSet(viewsets.ModelViewSet):
    queryset = Pension.objects.all()
    serializer_class = PensionSerializer

    def create(self, request, *args, **kwargs):
        request.data["owner"] = request.user.pk
        return super().create(request, *args, **kwargs)