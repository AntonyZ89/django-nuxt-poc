from rest_framework import serializers
from ..models import User


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ["email", "password", "role"]
