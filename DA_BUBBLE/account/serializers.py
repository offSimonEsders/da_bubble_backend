from rest_framework import serializers
from .models import DA_Bubble_User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})
    
    class Meta:
        model = DA_Bubble_User
        fields = ['username', 'email', 'password', 'avatar']
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = DA_Bubble_User.objects.create(**validated_data)
        return user