from django.core.exceptions import ValidationError
from django.db import models

from students.models import Student


class Unirecord(models.Model):
    name = models.CharField(max_length=50)
    record_date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE,
                                  # null=True, blank=True,
                                  # related_name='from_city_set',
                                  # verbose_name='Из какого города'
                                  )


#     def __str__(self):
#         return f'Поезд №{self.name} из города {self.from_city}'
#
    class Meta:
        # verbose_name = 'Поезд'
        # verbose_name_plural = 'Поезда'
        ordering = ['record_date']
#
#     def clean(self):
#         if self.from_city == self.to_city:
#             raise ValidationError('Изменить город прибытия')
#         qs = Train.objects.filter(
#             from_city=self.from_city, to_city=self.to_city,
#             travel_time=self.travel_time).exclude(pk=self.pk)
#         # Train == self.__class__
#         if qs.exists():
#             raise ValidationError('Измените время в пути')
#
#     def save(self, *args, **kwargs):
#         self.clean()
#         super().save(*args, **kwargs)
