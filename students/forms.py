from django import forms

from students.models import Student


class StudentForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя студента'
    }))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите фамилию студента'
    }))

    class Meta:
        model = Student
        fields = ('name', 'surname',)
