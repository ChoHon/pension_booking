from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="accounts-signup"),
    path("login/", LoginView.as_view(), name="accounts-login"),
]