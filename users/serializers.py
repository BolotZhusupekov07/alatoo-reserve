from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=False)
    surname = serializers.CharField(max_length=200, required=False)
    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["name", "surname", "email", "password"]


class LoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ["email", "password"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]
