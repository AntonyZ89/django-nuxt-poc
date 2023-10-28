from rest_framework import serializers
from ..models import DisciplineStudent


class DisciplineStudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = DisciplineStudent
        fields = '__all__'
        extra_kwargs = {
            'user': {
                'error_messages': {
                    'does_not_exist': "User doesn't exist or isn't a Student."
                }
            }
        }
