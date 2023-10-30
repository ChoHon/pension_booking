from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError

from .models import User
from .serializers import SignupSerializer

class SignUpView(APIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Response(serializer.data)
        else:
            if "email" in serializer.errors and "already" in serializer.errors["email"][0]:
                raise ValidationError("이미 사용 중인 이메일")
            else:
                raise ValidationError()