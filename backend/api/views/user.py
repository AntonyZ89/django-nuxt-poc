from rest_framework import viewsets, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from ..models import User
from ..serializers import (
    UserSerializer, TeacherSerializer, StudentSerializer, CoordinatorSerializer
)
from drf_spectacular.utils import OpenApiTypes, OpenApiParameter


class UserView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update'] and 'role' in self.request.data:
            match self.request.data.get('role'):
                case User.Role.TEACHER:
                    return TeacherSerializer
                case User.Role.STUDENT:
                    return StudentSerializer
                case User.Role.COORDINATOR:
                    return CoordinatorSerializer

        return UserSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        query = self.queryset

        if self.action == 'list':
            role = query_params.get('role')
            not_discipline = query_params.get('not_discipline')
            email = query_params.get('email')
            name = query_params.get('name')

            if role is not None:
                query = query.filter(role=role)

            if not_discipline is not None:
                query = query.exclude(
                    disciplinestudent__discipline__pk__in=not_discipline
                )

            if email is not None:
                query = query.filter(email__contains=email)

            if name is not None:
                query = query.filter(name__contains=name)

        return query.order_by('-created_at')

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
            OpenApiParameter(
                'email',
                type=OpenApiTypes.STR,
                description="Filter by email"
            ),
            OpenApiParameter(
                'name',
                type=OpenApiTypes.STR,
                description="Filter by name"
            ),
        ]
    )
    def list(self, request):
        return super().list(request)
