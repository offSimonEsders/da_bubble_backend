from rest_framework import serializers
from .models import DA_Bubble_User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DA_Bubble_User
        fields = ['username', 'email', 'password', 'avatar']