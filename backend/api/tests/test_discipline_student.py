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
        self.assertEqual(students[0]['note_1'], None)
        self.assertEqual(students[0]['note_2'], None)
        self.assertEqual(serializer.data.get('media'), None)
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

    def test_add_only_one_note(self):
        data = dict(
            user=self.student_id,
            discipline=self.discipline_id,
            note_1=5
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
        self.assertEqual(discipline_serializer.data.get('total_students'), 1)
        self.assertEqual(serializer.data.get('media'), 2.5)

    def test_add_two_notes(self):
        data = dict(
            user=self.student_id,
            discipline=self.discipline_id,
            note_1=5,
            note_2=10
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
        self.assertEqual(discipline_serializer.data.get('total_students'), 1)
        self.assertEqual(serializer.data.get('media'), 7.5)

    def test_add_note_zero(self):
        data = dict(
            user=self.student_id,
            discipline=self.discipline_id,
            note_1=0
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
        self.assertEqual(discipline_serializer.data.get('total_students'), 1)
        self.assertEqual(serializer.data.get('media'), 0)

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

    def test_add_note_less_than_0(self):
        data = dict(
            user=self.student_id,
            discipline=self.discipline_id,
            note_1=-1,
            note_2=-1,
        )

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineStudentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error1 = e.exception.detail['note_1'][0]
        error2 = e.exception.detail['note_2'][0]

        self.assertEqual(
            error1,
            "Ensure this value is greater than or equal to 0."
        )
        self.assertEqual(
            error2,
            "Ensure this value is greater than or equal to 0."
        )

    def test_add_note_more_than_10(self):
        data = dict(
            user=self.student_id,
            discipline=self.discipline_id,
            note_1=11,
            note_2=11,
        )

        with self.assertRaises(ValidationError) as e:
            serializer = DisciplineStudentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error1 = e.exception.detail['note_1'][0]
        error2 = e.exception.detail['note_2'][0]

        self.assertEqual(
            error1,
            "Ensure this value is less than or equal to 10."
        )
        self.assertEqual(
            error2,
            "Ensure this value is less than or equal to 10."
        )
