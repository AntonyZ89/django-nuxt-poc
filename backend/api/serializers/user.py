from rest_framework import serializers
from ..models import User, Teacher, Student, Coordinator


class UserSerializer (serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        match validated_data['role']:
            case User.Role.STUDENT:
                return Student.objects.create_user(**validated_data)
            case User.Role.TEACHER:
                return Teacher.objects.create_user(**validated_data)
            case User.Role.COORDINATOR:
                return Coordinator.objects.create_user(**validated_data)
