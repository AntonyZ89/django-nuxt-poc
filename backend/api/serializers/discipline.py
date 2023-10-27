from rest_framework import serializers
from ..models import Discipline


class DisciplineSerializer (serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'
