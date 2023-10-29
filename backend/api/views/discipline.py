from rest_framework import viewsets, permissions
from api.serializers import DisciplineSerializer
from django.db.models import Q
from api.models import Discipline
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes


class DisciplineView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DisciplineSerializer

    def get_queryset(self):
        query = self.request.query_params

        teacher = query.get('teacher')
        name = query.get('name')

        conditions = Q()

        if teacher is not None:
            conditions |= Q(teacher__name__contains=teacher)

        if name is not None:
            conditions |= Q(name__contains=name)

        return Discipline.objects.filter(conditions).order_by('-created_at')

    @extend_schema(
        parameters=[
            OpenApiParameter(
                'teacher',
                type=OpenApiTypes.STR,
                description="Filter by teacher's name"
            ),
            OpenApiParameter(
                'name',
                type=OpenApiTypes.STR,
                description="Filter by discipline's name"
            ),
        ]
    )
    def list(self, request):
        return super().list(request)
