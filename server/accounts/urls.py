from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="accounts-signup"),
    path("login/", LoginView.as_view(), name="accounts-login"),
    path("logout/", LogoutView.as_view(), name="accounts-logout"),
    path("refresh/", CustomTokenRefreshView.as_view(), name="accounts-refresh"),
]