# from django.core.exceptions import ValidationError
from django.db import models
from students.models import Student



class Unirecord(models.Model):
    record_name = models.CharField(max_length=50)
    record_date = models.DateField(null=True, blank=True)
    record_time = models.TimeField(null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


    def __str__(self):
        return f'Запись {self.record_name} от {self.record_date} время {self.record_time}'

    class Meta:
        ordering = ['record_date', 'record_time']
