from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import UserSerializer
from rest_framework.response import Response
from django.core import serializers

from .models import DA_Bubble_User

class registerApiViewSet(APIView):
    
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = DA_Bubble_User.objects.all()
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        return Response({'response': f'{serializer.is_valid()}'},status=status.HTTP_200_OK)