from datetime import date
from rest_framework import serializers
from ..models import Coordinator
from .user import UserSerializer


class CoordinatorSerializer (serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        model = Coordinator
        extra_kwargs = dict({
            "role": {"required": False, "default": Coordinator.base_role}
        }, **UserSerializer.Meta.extra_kwargs)

    def validate_birthday(self, value: date):
        today = date.today()
        age = today.year - value.year - \
            ((today.month, today.day) < (value.month, value.day))

        if age < 18:
            raise serializers.ValidationError(
                "Coordinator must be at least 18 years old"
            )

        return value

    def create(self, validated_data):
        return Coordinator.objects.create_user(**validated_data)
