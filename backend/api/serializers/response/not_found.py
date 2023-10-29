from rest_framework import serializers


class NotFoundSerializer(serializers.Serializer):
    message = serializers.CharField()
