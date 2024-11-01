from django.db import IntegrityError
from rest_framework.views import APIView, status, Request, Response
from users.models import User
from django.forms import model_to_dict
from django.contrib.auth import authenticate
from users.serializers import  UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import CustomPermission

class UserView(APIView):
    permission_classes = []
    def post(self, request):  
        serializer = UserSerializer(data=request.data)  
        if not serializer.is_valid():  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

        user = serializer.save()  
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)  

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CustomPermission]

    
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"message": "Usuario nao encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"message": "Usuario nao encontrado"}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"message": "Usuario nao encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        for key, value in serializer.validated_data.items():
            setattr(user, key, value)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

