from .discipline import Discipline
from django.db import models
from ..models.entity.user import User


class DisciplineNote(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        limit_choices_to={'role': User.Role.STUDENT}
    )

    note = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
