from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=30, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    # 로그인 로직
    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        user = authenticate(email=email, password=password)
        
        if user:
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)

            result = {
                'refresh': refresh_token,
                'access' : access_token
            }

            return result                      
        else:
            raise serializers.ValidationError()