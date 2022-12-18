# from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# from django.core.paginator import Paginator
# from django.shortcuts import render #, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from students.models import Student

from students.forms import StudentForm

__all__ = (
    'StudentDetailView',
    'StudentCreateView',
    'StudentUpdateView',
    'StudentDeleteView',
    'StudentListView',
)

class StudentListView(ListView):
    paginate_by = 3
    model = Student
    template_name = 'students/home.html'

class StudentDetailView(DetailView):
    queryset = Student.objects.all()
    template_name = 'students/detail.html'

class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/create.html'
    success_url = reverse_lazy('students:home')
    success_message = "Студент успешно создан"

class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/update.html'
    success_url = reverse_lazy('students:home')
    success_message = "Студент успешно отредактирован"

class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = reverse_lazy('students:home')
    success_message = "Студент успешно удален"
