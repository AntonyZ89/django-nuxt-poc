from rest_framework import serializers
from ..models import DisciplineNote


class DisciplineNoteSerializer (serializers.ModelSerializer):
    class Meta:
        model = DisciplineNote
        fields = '__all__'
