from rest_framework import serializers
from ..models import Student
from .user import UserSerializer


class StudentSerializer (serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        model = Student
        extra_kwargs = dict({
            "role": {"required": False, "default": Student.base_role}
        }, **UserSerializer.Meta.extra_kwargs)

    def create(self, validated_data):
        return Student.objects.create_user(**validated_data)

    def update(self, instance: Student, validated_data):
        return Student.objects.update_user(instance, **validated_data)
