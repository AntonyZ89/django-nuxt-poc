from datetime import datetime
from django.test import TestCase
from api.models import Discipline
from api.serializers import DisciplineSerializer
from rest_framework.exceptions import ValidationError


class DisciplineTest(TestCase):
    fixtures = ['student_fixture', 'teacher_fixture', 'coordinator_fixture']

    name = 'discipline'
    workload = 200
    student_id = 1
    teacher_id = 2
    coordinator_id = 3

    data = {
        'name': name,
        'workload': workload,
        'teacher': teacher_id
    }

    """
    Success cases
    """

    def test_create_discipline(self):
        """
        Test creating a discipline
        """

        serializer = DisciplineSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        discipline = serializer.instance

        self.assertEqual(discipline.pk, 1)
        self.assertEqual(discipline.name, self.name)
        self.assertEqual(discipline.workload, self.workload)
        self.assertEqual(discipline.teacher_id, self.teacher_id)
        self.assertIsInstance(discipline.created_at, datetime)
        self.assertIsInstance(discipline.updated_at, datetime)

    def test_update_discipline(self):
        """
        Test updating a discipline
        """
        serializer = DisciplineSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        discipline = Discipline.objects.get(pk=1)

        serializer = DisciplineSerializer(
            discipline,
            data={'name': 'New Name', 'workload': 150},
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        discipline = Discipline.objects.get(pk=1)

        self.assertEqual(discipline.name, 'New Name')
        self.assertEqual(discipline.workload, 150)

    """
    Fail cases
    """

    def test_create_discipline_without_teacher(self):
        """
        Test creating a discipline without teacher
        """

        data = dict(self.data, teacher=None)

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineSerializer(data=data)
            serializer.is_valid(raise_exception=True)

        error = e.exception.detail['teacher'][0]

        self.assertEqual(
            error,
            'This field may not be null.'
        )

    def test_create_discipline_with_teacher_that_does_not_exist(self):
        """
        Test creating a discipline with teacher that does not exist
        """

        data = dict(self.data, teacher=999)

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineSerializer(data=data)
            serializer.is_valid(raise_exception=True)

        error = e.exception.detail['teacher'][0]

        self.assertEqual(
            error,
            "User doesn't exist or isn't a Teacher."
        )

    def test_create_discipline_with_student(self):
        """
        Test creating a discipline with student as teacher
        """

        data = dict(self.data, teacher=self.student_id)

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineSerializer(data=data)
            serializer.is_valid(raise_exception=True)

        error = e.exception.detail['teacher'][0]

        self.assertEqual(
            error,
            "User doesn't exist or isn't a Teacher."
        )

    def test_create_discipline_with_coordinator(self):
        """
        Test creating a discipline with coordinator as teacher
        """

        data = dict(self.data, teacher=self.coordinator_id)

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineSerializer(data=data)
            serializer.is_valid(raise_exception=True)

        error = e.exception.detail['teacher'][0]

        self.assertEqual(
            error,
            "User doesn't exist or isn't a Teacher."
        )
