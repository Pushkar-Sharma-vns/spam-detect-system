from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ['name', 'phone', 'password', 'email', 'created_at']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class UserLoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, read_only=True)
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=128, write_only=True)
    
    def validate(self, data):
        phone = data.get('phone')
        password = data.get('password')
        
        if phone is None:
            raise serializers.ValidationError('Phone number is required for logging in.')
        
        if password is None:
            raise serializers.ValidationError('Password is required for logging in.')
        
        user = authenticate(username=phone, password=password)
        if user is None:
            raise serializers.ValidationError('Email or password is wrong, please enter data correctly!')
        if not user.is_active:
            raise serializers.ValidationError('This user is deactivated.')
        
        return{
            'name': user.name,
            'phone': user.phone
        }