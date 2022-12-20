from django import forms

from exercises.models import Exercise


class ExerciseForm(forms.ModelForm):
    exercise_name = forms.CharField(label='Код упражнения', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите код упражнения'
    }))
    exercise_description = forms.CharField(label='Описание упражнения', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Введите описание упражнения'
    }))

    class Meta:
        model = Exercise
        fields = ('exercise_name', 'exercise_description',)
