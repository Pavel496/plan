from django import forms
import datetime
from students.models import Student
from unirecords.models import Unirecord
from exercises.models import Exercise


class UnirecordForm(forms.ModelForm):
    record_name = forms.CharField(label='Универсальная запись', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите характеристику записи'
    }))        # , required=True
    exercise = forms.ModelChoiceField(
        label='Код упражнения',
        queryset=Exercise.objects.all(), widget=forms.Select(attrs={
            'class': 'form-control'
    }))
    student = forms.ModelChoiceField(
        label='Имя студента',
        queryset=Student.objects.all(), widget=forms.Select(attrs={
            'class': 'form-control'
    }))
    flights_number = forms.IntegerField(label='Количество полетов', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите количество полетов'
    }))
    flights_time = forms.TimeField(label='Налет', widget=forms.TimeInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите налет'
    }))
    record_date = forms.DateField(label='Дата', initial=datetime.date.today, widget=forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите дату'
    }))
    record_time = forms.TimeField(label='Время', initial=datetime.datetime.now(), widget=forms.TimeInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите время'}))



    class Meta:
        model = Unirecord
        fields = '__all__'
