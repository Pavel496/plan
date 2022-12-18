from django import forms
from students.models import Student
from unirecords.models import Unirecord


class UnirecordForm(forms.ModelForm):
    name = forms.CharField(label='Универсальная запись', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите характеристику записи'
    }))
    # record_date = forms.DateField(label='Дата', widget=forms.DateField(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Введите дату'})
    # )
    student = forms.ModelChoiceField(
        label='Имя студента',
        queryset=Student.objects.all(), widget=forms.Select(attrs={'class': 'form-control'})
    )


    class Meta:
        model = Unirecord
        fields = '__all__'
