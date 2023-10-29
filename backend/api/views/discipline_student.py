from rest_framework import viewsets, permissions, mixins
from api.serializers import DisciplineStudentSerializer
from api.models import DisciplineStudent
from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiParameter


class DisciplineStudentView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DisciplineStudentSerializer
    queryset = DisciplineStudent.objects.all()

    def get_queryset(self):
        condition = Q()

        if self.action == 'list':
            query = self.request.query_params
            student_name = query.get('student_name')
            discipline_id = query.get('discipline_id')

            # required field
            if discipline_id is None:
                return DisciplineStudent.objects.none()

            if student_name is not None:
                condition |= Q(user__name__contains=student_name)

            return (
                DisciplineStudent
                .objects
                .filter(discipline__id=discipline_id)
                .filter(condition)
            )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                'student_name',
                type=OpenApiTypes.STR,
                description="Filter by student's name"
            ),
            OpenApiParameter(
                'discipline_id',
                type=OpenApiTypes.STR,
                required=True,
                description="Filter by discipline's id"
            ),
        ]
    )
    def list(self, request):
        return super().list(request)
