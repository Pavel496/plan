# from django.core.exceptions import ValidationError
from django.db import models


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=20)
    exercise_description = models.CharField(max_length=200)

    def __str__(self):
        return self.exercise_name

    class Meta:
        ordering = ['exercise_name']
