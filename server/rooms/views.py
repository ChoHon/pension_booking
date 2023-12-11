from rest_framework import status, viewsets
from rest_framework.response import Response
from rooms.models import Room
from rooms.serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(
            pension=request.query_params['pension'], 
            pension__user=request.user
        )
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs["pk"], pension__user=request.user)

        serializer = RoomSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs["pk"], pension__user=request.user)

        serializer = RoomSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs["pk"], pension__user=request.user)
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)