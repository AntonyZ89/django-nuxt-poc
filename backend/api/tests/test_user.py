from api.serializers import (
    UserSerializer, StudentSerializer, TeacherSerializer, CoordinatorSerializer
)
from django.test import TestCase
from api.models import User, Student, Teacher, Coordinator
from rest_framework.exceptions import ValidationError


class AuthTest(TestCase):
    name = 'test'
    email = 'test@user.com'
    password = '12345678'
    birthday = '1999-01-01'

    data = {
        'name': name,
        'email': email,
        'password': password,
        'birthday': birthday
    }

    """
    Success cases
    """

    def test_create_user_as_student(self):
        """
        Test creating a user with the role of a student.
        """

        role = User.Role.STUDENT
        data = dict({'role': role}, **self.data)

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = serializer.instance

        self.assertEqual(user.pk, 1)
        self.assertEqual(user.email, self.email)
        self.assertNotEqual(user.password, self.password)
        self.assertEqual(user.role, role)
        self.assertEqual(user.birthday.strftime('%Y-%m-%d'), self.birthday)

    def test_create_user_as_teacher(self):
        """
        Test creating a user with the role of a teacher.
        """

        role = User.Role.TEACHER
        data = dict({'role': role}, **self.data)

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = serializer.instance

        self.assertEqual(user.pk, 1)
        self.assertEqual(user.email, self.email)
        self.assertNotEqual(user.password, self.password)
        self.assertEqual(user.role, role)
        self.assertEqual(user.birthday.strftime('%Y-%m-%d'), self.birthday)

    def test_create_user_as_coordinator(self):
        """
        Test creating a user with the role of a coordinator.
        """

        role = User.Role.COORDINATOR
        data = dict({'role': role}, **self.data)

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = serializer.instance

        self.assertEqual(user.pk, 1)
        self.assertEqual(user.email, self.email)
        self.assertNotEqual(user.password, self.password)
        self.assertEqual(user.role, role)
        self.assertEqual(user.birthday.strftime('%Y-%m-%d'), self.birthday)

    def test_filter_by_role_using_role_model(self):
        """
        Test filtering users by role using the corresponding serializers.
        """
        student_serializer = StudentSerializer(data=self.data)
        student_serializer.is_valid(raise_exception=True)
        student_serializer.save()

        teacher_serializer = TeacherSerializer(data=self.data)
        teacher_serializer.is_valid(raise_exception=True)
        teacher_serializer.save()

        coordinator_serializer = CoordinatorSerializer(data=self.data)
        coordinator_serializer.is_valid(raise_exception=True)
        coordinator_serializer.save()

        student = Student.objects.get(email=self.email)
        teacher = Teacher.objects.get(email=self.email)
        coordinator = Coordinator.objects.get(email=self.email)

        self.assertEqual(student.role, User.Role.STUDENT)
        self.assertEqual(teacher.role, User.Role.TEACHER)
        self.assertEqual(coordinator.role, User.Role.COORDINATOR)

    """
    Fail cases
    """

    def test_create_without_role(self):
        """
        Test creating a user without role
        """

        with self.assertRaises(ValidationError) as e:
            serializer = UserSerializer(data=self.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['role'][0]

        self.assertEqual(
            error,
            'This field is required.'
        )
