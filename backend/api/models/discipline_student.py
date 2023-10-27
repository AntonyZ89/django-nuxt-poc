from django.db import models
from .entity import Student


class DisciplineStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
