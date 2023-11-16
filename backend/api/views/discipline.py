from rest_framework import viewsets, permissions, status
from api.serializers import DisciplineSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from api.models import Discipline, DisciplineStudent, Student
from drf_spectacular.utils import (
    extend_schema, OpenApiParameter, OpenApiTypes, OpenApiExample
)


class DisciplineView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()

    def get_queryset(self):
        query_query = self.request.query_params
        query = self.queryset

        teacher = query_query.get('teacher')
        name = query_query.get('name')
        if teacher is not None:
            query = query.filter(teacher__name__contains=teacher)

        if name is not None:
            query = query.filter(name__contains=name)

        return query.order_by('-created_at')

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
            OpenApiParameter(
                'expand',
                type=OpenApiTypes.STR,
                description="Expand related fields",
                examples=[
                    OpenApiExample(
                        'expand',
                        value='students',
                        description="Expand students"
                    )
                ]
            ),
        ]
    )
    def list(self, request: Request):
        return super().list(request)

    def create(self, request: Request):
        students_data = request.data.pop('students', None)

        discipline_serializer = DisciplineSerializer(data=request.data)
        discipline_serializer.is_valid(raise_exception=True)
        discipline_serializer.save()

        discipline = discipline_serializer.instance

        DisciplineStudent.objects.bulk_create(
            DisciplineStudent(discipline=discipline, user_id=student)
            for student in students_data
        )

        return Response(
            DisciplineSerializer(discipline).data,
            status=status.HTTP_201_CREATED
        )

    def update(self, request: Request, pk: int):
        students_data = request.data.pop('students', None)

        discipline_serializer = DisciplineSerializer(
            Discipline.objects.get(pk=pk),
            data=request.data,
        )
        discipline_serializer.is_valid(raise_exception=True)
        discipline_serializer.save()

        student_ids = [
            student.pk for student in Student.objects.filter(
                disciplinestudent__discipline__pk=pk
            )
        ]

        if students_data is not None:
            new_ids = [
                student_data_id
                for student_data_id in students_data
                if student_data_id not in student_ids
            ]
            deleted_ids = [
                student_id
                for student_id in student_ids
                if student_id not in students_data
            ]

            DisciplineStudent.objects.filter(user__in=deleted_ids).delete()
            DisciplineStudent.objects.bulk_create(
                DisciplineStudent(discipline_id=pk, user_id=student_id)
                for student_id in new_ids
            )

        return Response(
            discipline_serializer.data,
            status=status.HTTP_200_OK
        )
