from . import User, UserManager


class CoordinatorManager(UserManager):
    def get_queryset(self):
        results = super().get_queryset()

        return results.filter(role=User.Role.COORDINATOR)


class Coordinator(User):
    base_role = User.Role.COORDINATOR

    objects = CoordinatorManager()

    class Meta:
        proxy = True
