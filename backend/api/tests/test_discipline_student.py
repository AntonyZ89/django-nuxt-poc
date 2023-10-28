from django.test import TestCase
from rest_framework.exceptions import ValidationError
from api.serializers import (
    DisciplineSerializer,
    TeacherSerializer,
    StudentSerializer,
    DisciplineStudentSerializer,
    CoordinatorSerializer
)
from api.models import Student


class DisciplineStudentTest(TestCase):
    student_id = 1
    teacher_id = 2
    coordinator_id = 3
    discipline_id = 1

    discipline_data = {
        'name': 'test',
        'workload': 200,
        'teacher': teacher_id
    }

    user_data = {
        'name': 'test user',
        'email': 'user@gmail.com',
        'password': '12345678',
        'birthday': '1999-01-01'
    }

    def setUp(self):
        student_serializer = StudentSerializer(data=self.user_data)
        student_serializer.is_valid(raise_exception=True)
        student_serializer.save()

        teacher_serializer = TeacherSerializer(data=self.user_data)
        teacher_serializer.is_valid(raise_exception=True)
        teacher_serializer.save()

        coordinator_serializer = CoordinatorSerializer(data=self.user_data)
        coordinator_serializer.is_valid(raise_exception=True)
        coordinator_serializer.save()

        discipline_serializer = DisciplineSerializer(data=self.discipline_data)
        discipline_serializer.is_valid(raise_exception=True)
        discipline_serializer.save()

    def test_vinculate_student_to_discipline(self):
        data = dict(
            user=self.student_id,
            discipline=self.discipline_id
        )

        serializer = DisciplineStudentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        students = Student.objects.filter(
            disciplinestudent__discipline__pk=self.discipline_id
        )

        self.assertEqual(len(students), self.student_id)
        self.assertEqual(students[0].pk, self.student_id)

    def test_vinculate_teacher_to_discipline(self):
        data = dict(
            user=self.teacher_id,
            discipline=self.discipline_id
        )

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineStudentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['user'][0]

        self.assertEqual(
            error,
            "User doesn't exist or isn't a Student."
        )

    def test_vinculate_coordinator_to_discipline(self):
        data = dict(
            user=self.coordinator_id,
            discipline=self.discipline_id
        )

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineStudentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['user'][0]

        self.assertEqual(
            error,
            "User doesn't exist or isn't a Student."
        )
