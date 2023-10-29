from rest_framework import viewsets, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from ..serializers import UserSerializer


class UserView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses={status.HTTP_200_OK: UserSerializer}
    )
    @action(detail=False, methods=["GET"])
    def me(self, request: Request):
        serializer = UserSerializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
