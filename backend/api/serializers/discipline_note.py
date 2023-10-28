from rest_framework import serializers
from ..models import DisciplineNote


class DisciplineNoteSerializer (serializers.ModelSerializer):
    note = serializers.IntegerField(min_value=0, max_value=10)

    class Meta:
        model = DisciplineNote
        fields = '__all__'
        extra_kwargs = {
            'user': {
                'error_messages': {
                    'does_not_exist': "User doesn't exist or isn't a Student."
                }
            }
        }
