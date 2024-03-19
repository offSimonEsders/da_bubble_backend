import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import UserSerializer
from rest_framework.response import Response

from .models import DA_Bubble_User

def save_image(image_data, file_path):
    with open(file_path, 'wb') as f:
        f.write(image_data)

class registerApiViewSet(APIView):
    
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = DA_Bubble_User.objects.all()
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)