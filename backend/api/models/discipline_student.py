from django.db import models
from .entity import Student
from .discipline import Discipline


class DisciplineStudent(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.RESTRICT)

    created_at = models.DateTimeField(auto_now_add=True)
