from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('complete/<int:pk>/', views.mark_completed, name='mark-completed'),
]


