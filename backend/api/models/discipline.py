from .entity import Teacher
from django.db import models


class Discipline(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT)

    name = models.CharField(max_length=50)
    workload = models.DecimalField(max_digits=4, decimal_places=2)

    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
