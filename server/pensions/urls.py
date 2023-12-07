from django.urls import include, path
from rest_framework.routers import DefaultRouter

from pensions import views

router = DefaultRouter()
router.register(r'', views.PensionViewSet, basename='pensions')

urlpatterns = [
    path('', include(router.urls)),
]