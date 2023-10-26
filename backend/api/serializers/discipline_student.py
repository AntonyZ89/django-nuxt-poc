from rest_framework import serializers
from ..models import DisciplineStudent


class DisciplineStudentSerializer (serializers.Serializer):
    class Meta:
        model = DisciplineStudent
        fields = '__all__'
