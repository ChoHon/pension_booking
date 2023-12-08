from rest_framework import status, viewsets
from rest_framework.response import Response
from pensions.models import Pension
from pensions.serializers import PensionSerializer

class PensionViewSet(viewsets.ModelViewSet):
    queryset = Pension.objects.all()
    serializer_class = PensionSerializer

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.pk
        return super().create(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(user=request.user)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs["pk"], user=request.user)

        serializer = PensionSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs["pk"], user=request.user)

        serializer = PensionSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs["pk"], user=request.user)
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)