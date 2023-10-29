from django.test import TestCase
from rest_framework.exceptions import ValidationError
from api.serializers import DisciplineStudentSerializer, DisciplineSerializer
from api.models import DisciplineStudent


class DisciplineStudentTest(TestCase):
    fixtures = [
        'student_fixture', 'teacher_fixture',
        'coordinator_fixture', 'discipline_fixture'
    ]

    student_id = 1
    teacher_id = 2
    coordinator_id = 3
    discipline_id = 1

    """
    Success cases
    """

    def test_vinculate_student_to_discipline(self):
        data = dict(
            user=self.student_id,
            discipline=self.discipline_id
        )

        serializer = DisciplineStudentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        discipline_serializer = DisciplineSerializer(
            serializer.instance.discipline,
            expand=['students'],
        )

        students = discipline_serializer.data.get('students')

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['id'], self.student_id)
        self.assertEqual(discipline_serializer.data.get('total_students'), 1)

    def test_unvinculate_student_to_discipline(self):
        data = dict(
            user=self.student_id,
            discipline=self.discipline_id
        )

        serializer = DisciplineStudentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        discipline_serializer = DisciplineSerializer(
            serializer.instance.discipline,
            expand=['students'],
        )

        DisciplineStudent.objects.filter(**data).delete()

        students = discipline_serializer.data.get('students')

        self.assertEqual(len(students), 0)
        self.assertEqual(discipline_serializer.data.get('total_students'), 0)

    """
    Fail cases
    """

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
