from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]


urlpatterns = [
    path('', views.task_list_create, name='task-list'),
]

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('complete/<int:pk>/', views.mark_completed, name='mark-completed'),
]
