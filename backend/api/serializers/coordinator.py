from rest_framework import serializers
from ..models import Coordinator


class CoordinatorSerializer (serializers.Serializer):
    class Meta:
        model = Coordinator
        fields = '__all__'
