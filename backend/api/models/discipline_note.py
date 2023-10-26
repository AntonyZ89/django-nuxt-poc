from .discipline import Discipline
from django.db import models


class DisciplineNote(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    note = models.FloatField()

    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
