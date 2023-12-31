from datetime import date
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from ..models import Teacher
from .user import UserSerializer


class TeacherSerializer (serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        model = Teacher
        extra_kwargs = dict({
            "role": {"required": False, "default": Teacher.base_role}
        }, **UserSerializer.Meta.extra_kwargs)

    def validate_birthday(self, value: date):
        today = date.today()
        age = today.year - value.year - \
            ((today.month, today.day) < (value.month, value.day))

        if age < 18:
            raise serializers.ValidationError(
                _("%(role)s must be at least 18 years old")
                %
                {"role": _("Teacher")}
            )

        return value

    def create(self, validated_data):
        return Teacher.objects.create_user(**validated_data)

    def update(self, instance: Teacher, validated_data):
        return Teacher.objects.update_user(instance, **validated_data)
