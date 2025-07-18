from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),

    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

    path('register/', views.register, name='register'),

    path('toggle-status/', views.toggle_task_status, name='toggle_task_status'),

]
