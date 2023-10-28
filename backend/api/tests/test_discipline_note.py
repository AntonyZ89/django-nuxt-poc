from django.test import TestCase
from rest_framework.exceptions import ValidationError
from api.serializers import (
    StudentSerializer,
    DisciplineNoteSerializer,
    TeacherSerializer,
    CoordinatorSerializer,
    DisciplineSerializer
)


class DisciplineNote(TestCase):
    student_id = 1
    teacher_id = 2
    coordinator_id = 3

    discipline_id = 1

    note = 10

    data = {
        'note': note,
        'user': student_id,
        'discipline': discipline_id
    }

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

    """
    Success test
    """

    def setUp(self):
        serializer = StudentSerializer(data=self.user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        serializer = TeacherSerializer(data=self.user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        serializer = CoordinatorSerializer(data=self.user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        serializer = DisciplineSerializer(data=self.discipline_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def test_create_discipline_note(self):
        serializer = DisciplineNoteSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        discipline_note = serializer.instance

        self.assertEqual(discipline_note.note, self.note)
        self.assertEqual(discipline_note.user_id, self.student_id)

    """
    Fail test
    """

    def test_create_discipline_note_with_note_less_than_0(self):
        data = dict(self.data, note=-1)

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineNoteSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['note'][0]

        self.assertEqual(
            error,
            'Ensure this value is greater than or equal to 0.'
        )

    def test_create_discipline_note_with_note_more_than_10(self):
        data = dict(self.data, note=11)

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineNoteSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['note'][0]

        self.assertEqual(
            error,
            'Ensure this value is less than or equal to 10.'
        )

    def test_create_discipline_note_without_note(self):
        data = dict(self.data, note=None)

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineNoteSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['note'][0]

        self.assertEqual(
            error,
            'This field may not be null.'
        )

    def test_create_discipline_note_without_student(self):
        data = dict(self.data, user=None)

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineNoteSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['user'][0]

        self.assertEqual(
            error,
            'This field may not be null.'
        )

    def test_create_discipline_note_with_teacher(self):
        data = dict(self.data, user=self.teacher_id)

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineNoteSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['user'][0]

        self.assertEqual(
            error,
            "User doesn't exist or isn't a Student."
        )

    def test_create_discipline_note_with_coordinator(self):
        data = dict(self.data, user=self.coordinator_id)

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineNoteSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['user'][0]

        self.assertEqual(
            error,
            "User doesn't exist or isn't a Student."
        )
