from rest_framework import serializers
from ..models import DisciplineNote


class DisciplineNoteSerializer (serializers.Serializer):
    class Meta:
        model = DisciplineNote
        fields = '__all__'
