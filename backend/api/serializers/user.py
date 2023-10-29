from rest_framework import serializers, validators
from ..models import User


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        validators = [
            validators.UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['email', 'role'],
                message='User with this email and role already exists'
            )
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
