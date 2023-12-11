from rest_framework import status, viewsets
from rest_framework.response import Response
from reservations.models import Reservation
from reservations.serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(
            room__pension__user=request.user
        )
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs["pk"], room__pension__user=request.user)

        serializer = ReservationSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs["pk"], room__pension__user=request.user)

        serializer = ReservationSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs["pk"], room__pension__user=request.user)
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)