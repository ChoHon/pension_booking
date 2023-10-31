from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import SignupSerializer, LoginSerializer

User = get_user_model()

# 회원가입 View
class SignUpView(APIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise ValidationError({"message" : "잘못된 입력"})
            
# 로그인 View
class LoginView(APIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data)
        else:
            raise ValidationError({"detail" : "잘못된 입력"})
        
# 로그아웃 View
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data["refresh"]
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_200_OK)
        except:
            return Response(data={"detail" : "잘못된 토큰"}, status=status.HTTP_401_UNAUTHORIZED)
        
# Refresh 토큰으로 Access 토큰 재발급 View
class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)        
        except:
            raise ValidationError({"detail" : "잘못된 토큰"})
        
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)