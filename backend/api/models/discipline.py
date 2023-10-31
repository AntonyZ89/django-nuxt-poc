from .entity import Teacher
from django.db import models


class Discipline(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        limit_choices_to={'role': Teacher.Role.TEACHER}
    )

    name = models.CharField(max_length=50)
    workload = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
