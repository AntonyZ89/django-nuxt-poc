from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.contrib import auth
from ..models import User
from ..serializers import LoginSerializer
from .. import permissions as custom_permissions


@api_view(["POST"])
@permission_classes([custom_permissions.IsGuest])
def login(request: Request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = auth.authenticate(**serializer.validated_data)

    if not user:
        return Response(
            {"message": "User not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    token, _ = Token.objects.get_or_create(user=user)

    User.objects.filter(pk=user.pk).update(last_login=timezone.now())

    return Response(
        {
            "message": "Log in successfully",
            "token": token.key,
        },
        status=status.HTTP_200_OK
    )
