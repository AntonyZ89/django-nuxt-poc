from django.test import TestCase
from api.models import Coordinator
from api.serializers import CoordinatorSerializer
from rest_framework.exceptions import ValidationError


class CoordinatorTest(TestCase):
    name = 'coordinator'
    email = 'coordinator@user.com'
    password = '12345678'
    birthday = '1999-01-01'
    role = Coordinator.Role.COORDINATOR

    data = {
        'name': name,
        'email': email,
        'password': password,
        'birthday': birthday
    }

    """
    Success cases
    """

    def test_create_coordinator(self):
        """
        Test creating a coordinator using the CoordinatorSerializer.
        """

        serializer = CoordinatorSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        coordinator = serializer.instance

        self.assertEqual(coordinator.pk, 1)
        self.assertEqual(coordinator.email, self.email)
        self.assertEqual(coordinator.role, self.role)
        self.assertNotEqual(coordinator.password, self.password)
        self.assertEqual(
            coordinator.birthday.strftime('%Y-%m-%d'),
            self.birthday
        )

    def test_update_coordinator(self):
        """
        Test updating a coordinator's name using the CoordinatorSerializer.
        """

        serializer = CoordinatorSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        coordinator = Coordinator.objects.get(email=self.email)

        serializer = CoordinatorSerializer(
            coordinator, data={'name': 'New Name'}, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        coordinator = Coordinator.objects.get(email=self.email)

        self.assertEqual(coordinator.name, 'New Name')

    def test_create_coordinator_age_more_than_18(self):
        """
        Test creating a coordinator with an age more than 18.
        """

        self.data['birthday'] = '1999-01-01'

        serializer = CoordinatorSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    """
    Fail cases
    """

    def test_create_coordinator_age_less_than_18(self):
        """
        Test creating a coordinator with an age less than 18.
        """

        self.data['birthday'] = '2010-01-01'

        with self.assertRaises(ValidationError) as e:
            serializer = CoordinatorSerializer(data=self.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['birthday'][0]

        self.assertEqual(
            error,
            'Coordinator must be at least 18 years old'
        )

    def test_create_duplicated_coordinator(self):
        """
        Test creating a duplicate coordinator and ensure it raises a ValidationError.
        """

        serializer = CoordinatorSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        with self.assertRaises(ValidationError) as e:
            serializer = CoordinatorSerializer(data=self.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        error = e.exception.detail['non_field_errors'][0]

        self.assertEqual(
            error,
            'User with this email and role already exists'
        )
