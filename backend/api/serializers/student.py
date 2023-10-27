from rest_framework import serializers
from ..models import Student
from .user import UserSerializer


class StudentSerializer (serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        model = Student
        extra_kwargs = {
            "role": {"required": False, "default": Student.base_role}
        }

    def create(self, validated_data):
        return Student.objects.create_user(**validated_data)
