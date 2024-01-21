
from django.urls import path

from habits.views.habit import PublicHabitsListView, HabitsListView, \
    HabitsCreateView, HabitsUpdateView, HabitsDeleteView, HabitsDetailView

urlpatterns = [
    path('', PublicHabitsListView.as_view(), name='public_list'),
    path('my/', HabitsListView.as_view(), name='private_list'),
    path('create/', HabitsCreateView.as_view(), name='create_habit'),
    path('<int:pk>/', HabitsDetailView.as_view(), name='detail_habit'),
    path('update/<int:pk>/', HabitsUpdateView.as_view(), name='update_habit'),
    path('delete/<int:pk>/', HabitsDeleteView.as_view(), name='delete_habit'),
]
