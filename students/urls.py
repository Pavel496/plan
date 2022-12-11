from django.urls import path

from students.views import *

urlpatterns = [
    path('', StudentListView.as_view(), name='home'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
    path('add/', StudentCreateView.as_view(), name='create'),

]