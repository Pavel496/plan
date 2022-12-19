from django import forms
import datetime
from students.models import Student
from unirecords.models import Unirecord


class UnirecordForm(forms.ModelForm):
    record_name = forms.CharField(label='Универсальная запись', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите характеристику записи'
    }))        # , required=True
    record_date = forms.DateField(label='Дата', initial=datetime.date.today, widget=forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите дату'
    }))
    record_time = forms.TimeField(label='Время', initial=datetime.time, widget=forms.TimeInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите время'}))
    student = forms.ModelChoiceField(
        label='Имя студента',
        queryset=Student.objects.all(), widget=forms.Select(attrs={
            'class': 'form-control'
    }))


    class Meta:
        model = Unirecord
        fields = '__all__'
