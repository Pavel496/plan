from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=50)  #, verbose_name = 'Имя'
    surname = models.CharField(max_length=50, blank=True)   #, verbose_name = 'Фамилия'

    def __str__(self):
        return self.surname

    class Meta:
        # verbose_name = 'Студент'
        # verbose_name_plural = 'Студенты'
        ordering = ['surname']

    def get_absolute_url(self):
        return reverse('students:detail', kwargs={'pk': self.pk})