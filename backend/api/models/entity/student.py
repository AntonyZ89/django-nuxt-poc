from . import User, UserManager


class StudentManager(UserManager):

    def get_queryset(self):
        results = super().get_queryset()

        return results.filter(role=User.Role.STUDENT)


class Student(User):
    base_role = User.Role.STUDENT

    objects = StudentManager()

    class Meta:
        proxy = True
