from datetime import date
from rest_framework import serializers
from ..models import Teacher
from .user import UserSerializer


class TeacherSerializer (serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        model = Teacher
        extra_kwargs = {
            "role": {"required": False, "default": Teacher.base_role}
        }

    def validate_birthday(self, value: date):
        today = date.today()
        age = today.year - value.year - \
            ((today.month, today.day) < (value.month, value.day))

        if age < 18:
            raise serializers.ValidationError(
                "Teacher must be at least 18 years old"
            )

        return value

    def create(self, validated_data):
        return Teacher.objects.create_user(**validated_data)
