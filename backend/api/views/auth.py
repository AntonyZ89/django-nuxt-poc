from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.openapi import OpenApiResponse, OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework.decorators import permission_classes, action
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.contrib import auth
from ..models import User
from ..serializers import LoginSerializer, NotFoundSerializer, TokenSerializer
from .. import permissions as custom_permissions


class AuthView(viewsets.ViewSet):
    serializer_class = LoginSerializer

    @extend_schema(
        responses={
            status.HTTP_404_NOT_FOUND: OpenApiResponse(response=NotFoundSerializer),
            status.HTTP_200_OK: OpenApiResponse(response=TokenSerializer),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=OpenApiTypes.JSON_PTR,
                examples=[
                    OpenApiExample(
                        'error',
                        value=dict(
                            field_name=["error message 1", "error message 2"]
                        )
                    )
                ]
            )
        }
    )
    @permission_classes([custom_permissions.IsGuest])
    @action(detail=False, methods=["POST"])
    def login(self, request: Request):
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
