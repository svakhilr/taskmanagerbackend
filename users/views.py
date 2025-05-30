from rest_framework.views import APIView
from .models import CustomUser
from .token import get_tokens_for_user
from rest_framework import status,serializers
from rest_framework.response import Response
from django.contrib.auth import authenticate

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class UserApiView(APIView):

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            if CustomUser.objects.filter(email= data["email"]).exists():
                return Response({"message":"Username already exists"},status=status.HTTP_400_BAD_REQUEST)
            data["role"] = CustomUser.USER
            user = CustomUser.objects.create_user(**data)
            tokens = get_tokens_for_user(user)
            return  Response({"tokens":tokens},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        print(email,password)
        user = authenticate(request,email=email, password=password)

        if user is not None:
            tokens = get_tokens_for_user(user)
            return  Response({"tokens":tokens},status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)