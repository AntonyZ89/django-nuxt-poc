from rest_framework import serializers
from ..models import Discipline


class DisciplineSerializer (serializers.Serializer):
    class Meta:
        model = Discipline
        fields = '__all__'
