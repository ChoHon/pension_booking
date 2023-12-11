from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pensions.views import PensionViewSet
from rooms.views import RoomViewSet
from reservations.views import ReservationViewSet

router = DefaultRouter()
router.register(r'pensions', PensionViewSet, basename='pensions')
router.register(r'rooms', RoomViewSet, basename='rooms')
router.register(r'reservations', ReservationViewSet, basename='reservations')

urlpatterns = [
    path('', include(router.urls)),
    path('accounts/', include('accounts.urls')),
]
