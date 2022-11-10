from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
    
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password) # 패스워드 해싱
        user.save()
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):   # jwt payload 커스텀
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['token_message'] = "sparta_time_attack"

        return token