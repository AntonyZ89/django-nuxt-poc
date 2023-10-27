from django.test import TestCase
from api.models import Teacher
from api.serializers import TeacherSerializer
from rest_framework.exceptions import ValidationError


class TeacherTest(TestCase):
    name = 'teacher'
    email = 'teacher@user.com'
    password = '12345678'
    birthday = '1999-01-01'
    role = Teacher.Role.TEACHER

    data = {
        'name': name,
        'email': email,
        'password': password,
        'birthday': birthday
    }

    """
    Success cases
    """

    def test_create_teacher(self):
        """
        Test creating a teacher using the TeacherSerializer.
        """

        serializer = TeacherSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        teacher = serializer.instance

        self.assertEqual(teacher.pk, 1)
        self.assertEqual(teacher.email, self.email)
        self.assertEqual(teacher.role, self.role)
        self.assertNotEqual(teacher.password, self.password)
        self.assertEqual(teacher.birthday.strftime('%Y-%m-%d'), self.birthday)

    def test_update_teacher(self):
        """
        Test updating a teacher's name using the TeacherSerializer.
        """

        serializer = TeacherSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        teacher = Teacher.objects.get(email=self.email)

        serializer = TeacherSerializer(
            teacher, data={'name': 'New Name'}, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        teacher = Teacher.objects.get(email=self.email)

        self.assertEqual(teacher.name, 'New Name')

    def test_create_teacher_age_more_than_18(self):
        """
        Test creating a teacher with an age more than 18.
        """

        self.data['birthday'] = '1999-01-01'

        serializer = TeacherSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    """
    Fail cases
    """

    def test_create_teacher_age_less_than_18(self):
        """
        Test creating a teacher with an age less than 18.
        """

        self.data['birthday'] = '2010-01-01'

        with self.assertRaises(ValidationError) as e:
            serializer = TeacherSerializer(data=self.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['birthday'][0]

        self.assertEqual(
            error,
            'Teacher must be at least 18 years old'
        )

    def test_create_duplicated_teacher(self):
        """
        Test creating a duplicate teacher and ensure it raises a ValidationError.
        """

        serializer = TeacherSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        with self.assertRaises(ValidationError) as e:
            serializer = TeacherSerializer(data=self.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['non_field_errors'][0]

        self.assertEqual(
            error,
            'User with this email and role already exists'
        )
