# from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# from django.core.paginator import Paginator
# from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView,
    ListView
)

from exercises.forms import ExerciseForm
from exercises.models import Exercise

__all__ = (
    # 'home',
    'ExerciseListView',
    'ExerciseDetailView',
    'ExerciseCreateView',
    'ExerciseUpdateView',
    'ExerciseDeleteView',
)

class ExerciseDeleteView(SuccessMessageMixin, DeleteView):
    model = Exercise
    template_name = 'exercises/delete.html'
    success_url = reverse_lazy('exercises:home')
    success_message = "Упражнение успешно удалено"

class ExerciseListView(ListView):
    paginate_by = 10
    model = Exercise
    template_name = 'exercises/home.html'


class ExerciseDetailView(DetailView):
    # form_class = ExerciseForm
    queryset = Exercise.objects.all()
    template_name = 'exercises/detail.html'


class ExerciseCreateView(SuccessMessageMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'exercises/create.html'
    success_url = reverse_lazy('exercises:home')
    success_message = "Упражнение успешно создано"


class ExerciseUpdateView(SuccessMessageMixin, UpdateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'exercises/update.html'
    success_url = reverse_lazy('exercises:home')
    success_message = "Упражнение успешно отредактировано"







    # def get(self, request, *args, **kwargs):
    #     messages.success(request, 'Поезд успешно удален')
    #     return self.post(request, *args, **kwargs)

# def home(request, pk=None):
#     qs = Train.objects.all()
#     lst = Paginator(qs, 5)
#     page_number = request.GET.get('page')
#     page_obj = lst.get_page(page_number)
#     context = {'page_obj': page_obj,}
#     return render(request, 'exercises/home.html', context)
