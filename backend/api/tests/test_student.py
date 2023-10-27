from django.test import TestCase
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.exceptions import ValidationError


class StudentTest(TestCase):
    name = 'student'
    email = 'student@user.com'
    password = '12345678'
    birthday = '1999-01-01'
    role = Student.Role.STUDENT

    data = {
        'name': name,
        'email': email,
        'password': password,
        'birthday': birthday
    }

    def test_create_student(self):
        serializer = StudentSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        student = serializer.instance

        self.assertEqual(student.pk, 1)
        self.assertEqual(student.email, self.email)
        self.assertEqual(student.role, self.role)
        self.assertNotEqual(student.password, self.password)
        self.assertEqual(student.birthday.strftime('%Y-%m-%d'), self.birthday)

    def test_update_student(self):
        serializer = StudentSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        student = Student.objects.get(email=self.email)

        serializer = StudentSerializer(
            student, data={'name': 'New Name'}, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        student = Student.objects.get(email=self.email)

        self.assertEqual(student.name, 'New Name')

    def test_create_duplicated_student(self):
        serializer = StudentSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        with self.assertRaises(ValidationError) as e:
            serializer = StudentSerializer(data=self.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['non_field_errors'][0]

        self.assertEqual(
            error,
            'User with this email and role already exists'
        )
