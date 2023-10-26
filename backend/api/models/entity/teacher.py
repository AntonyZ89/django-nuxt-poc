from . import User, UserManager


class TeacherManager(UserManager):
    def get_queryset(self):
        results = super().get_queryset()

        return results.filter(role=User.Role.TEACHER)


class Teacher(User):
    base_role = User.Role.TEACHER

    objects = TeacherManager()

    class Meta:
        proxy = True
