from rest_framework import serializers
from ..models import DisciplineStudent


class DisciplineStudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = DisciplineStudent
        fields = '__all__'
