from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasks_home, name='tasks_home'),
    path('api/tasks/complete/<int:pk>/', views.mark_complete_api, name='api-mark-complete'),
    path('api/tasks/', views.task_api, name='task-api'),  
]
