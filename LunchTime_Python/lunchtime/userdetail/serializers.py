from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def validate_email(self, email):
        if not email.endswith("@simformsolutions.com"):
            raise serializers.ValidationError('enter valid email address')
        return email


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfilegetSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(many=False)
    class Meta:
        model = Profile
        fields = '__all__'
