from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView
from .views import *

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="accounts-signup"),
    path("login/", LoginView.as_view(), name="accounts-login"),
    path("logout/", LogoutView.as_view(), name="accounts-logout"),
    path("verify/", TokenVerifyView.as_view(), name="accounts-verify"),
    path("refresh/", TokenRefreshView.as_view(), name="accounts-refresh"),
]