from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView,
    ListView
)

from unirecords.forms import UnirecordForm
from unirecords.models import Unirecord

__all__ = (
    'UnirecordListView',
    'UnirecordDetailView',
    'UnirecordCreateView',
    'UnirecordUpdateView',
    'UnirecordDeleteView',
)

class UnirecordDeleteView(SuccessMessageMixin, DeleteView):
    model = Unirecord
    template_name = 'unirecords/delete.html'
    success_url = reverse_lazy('unirecords:home')
    success_message = "Универсальная запись успешно удалена"

class UnirecordListView(ListView):
    paginate_by = 10
    model = Unirecord
    template_name = 'unirecords/home.html'


class UnirecordDetailView(DetailView):
    # form_class = UnirecordForm
    queryset = Unirecord.objects.all()
    template_name = 'unirecords/detail.html'


class UnirecordCreateView(SuccessMessageMixin, CreateView):
    model = Unirecord
    form_class = UnirecordForm
    template_name = 'unirecords/create.html'
    success_url = reverse_lazy('unirecords:home')
    success_message = "Запись успешно создана"


class UnirecordUpdateView(SuccessMessageMixin, UpdateView):
    model = Unirecord
    form_class = UnirecordForm
    template_name = 'unirecords/update.html'
    success_url = reverse_lazy('unirecords:home')
    success_message = "Запись успешно отредактирована"
