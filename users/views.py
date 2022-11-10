from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Create your views here.
class UserView(APIView):
    def post(self, request):  # 회원가입
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
class CustomTokenObtainPairView(TokenObtainPairView): # jwt payload 커스텀
    serializer_class = CustomTokenObtainPairSerializer
