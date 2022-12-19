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

from unirecords.forms import UnirecordForm
from unirecords.models import Unirecord

__all__ = (
    # 'home',
    'UnirecordListView',
    'UnirecordDetailView',
    'UnirecordCreateView',
    'UnirecordUpdateView',
    'UnirecordDeleteView',
)

class UnirecordDeleteView(SuccessMessageMixin, DeleteView):
    model = Unirecord
    template_name = 'exercises/delete.html'
    success_url = reverse_lazy('exercises:home')
    success_message = "Универсальная запись успешно удалена"

class UnirecordListView(ListView):
    paginate_by = 10
    model = Unirecord
    template_name = 'exercises/home.html'


class UnirecordDetailView(DetailView):
    # form_class = UnirecordForm
    queryset = Unirecord.objects.all()
    template_name = 'exercises/detail.html'


class UnirecordCreateView(SuccessMessageMixin, CreateView):
    model = Unirecord
    form_class = UnirecordForm
    template_name = 'exercises/create.html'
    success_url = reverse_lazy('exercises:home')
    success_message = "Запись успешно создана"


class UnirecordUpdateView(SuccessMessageMixin, UpdateView):
    model = Unirecord
    form_class = UnirecordForm
    template_name = 'exercises/update.html'
    success_url = reverse_lazy('exercises:home')
    success_message = "Запись успешно отредактирована"







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
