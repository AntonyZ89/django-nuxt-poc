from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def update_user(self, user, **kwargs):
        for key, value in kwargs.items():
            if key == 'password':
                user.set_password(value)
            elif key == 'email':
                user.email = self.normalize_email(value)
            else:
                setattr(user, key, value)

        user.save()

        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault('name', 'Admin')
        extra_fields.setdefault('role', User.Role.COORDINATOR)
        extra_fields.setdefault('birthday', '1999-01-01')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    class Role(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        TEACHER = 'TEACHER', 'Teacher'
        COORDINATOR = 'COORDINATOR', 'Coordinator'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'role'],
                name='unique_email_role'
            )
        ]

    USERNAME_FIELD = 'email'

    objects = UserManager()

    name = models.CharField(max_length=50)
    email = models.EmailField()
    birthday = models.DateField()

    role = models.CharField(max_length=30, choices=Role.choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
