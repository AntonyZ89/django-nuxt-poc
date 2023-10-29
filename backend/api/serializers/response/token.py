from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    message = serializers.CharField()
    token = serializers.CharField()
