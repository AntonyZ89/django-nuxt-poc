from rest_framework import serializers
from ..models import Discipline


class DisciplineSerializer (serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'
        extra_kwargs = {
            'teacher': {
                'error_messages': {
                    'does_not_exist': "User doesn't exist or isn't a Teacher."
                }
            }
        }
