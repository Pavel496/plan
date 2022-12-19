from django.urls import path

from exercises.views import *

urlpatterns = [
    # path('', home, name='home'),
    path('', ExerciseListView.as_view(), name='home'),
    path('detail/<int:pk>/', ExerciseDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', ExerciseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ExerciseDeleteView.as_view(), name='delete'),
    path('add/', ExerciseCreateView.as_view(), name='create'),

]