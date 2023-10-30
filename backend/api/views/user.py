from rest_framework import viewsets, permissions, status, mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from ..models import User
from ..serializers import UserSerializer
from drf_spectacular.utils import OpenApiTypes, OpenApiParameter


class UserView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        query = self.queryset

        if self.action == 'list':
            role = self.request.query_params.get('role')
            not_discipline = self.request.query_params.get('not_discipline')

            if role is not None:
                query = query.filter(role=role)

            if not_discipline is not None:
                query = query.exclude(
                    disciplinestudent__discipline__pk__in=not_discipline
                )

        return query

    @extend_schema(
        responses={status.HTTP_200_OK: UserSerializer}
    )
    @action(detail=False, methods=["GET"])
    def me(self, request: Request):
        serializer = UserSerializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                'role',
                type=OpenApiTypes.STR,
                enum=User.Role,
                description="Filter by role"
            ),
        ]
    )
    def list(self, request):
        return super().list(request)
