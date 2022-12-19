from django.urls import path

from unirecords.views import *

urlpatterns = [
    # path('', home, name='home'),
    path('', UnirecordListView.as_view(), name='home'),
    path('detail/<int:pk>/', UnirecordDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', UnirecordUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', UnirecordDeleteView.as_view(), name='delete'),
    path('add/', UnirecordCreateView.as_view(), name='create'),

]