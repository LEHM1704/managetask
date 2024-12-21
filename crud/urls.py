from django.urls import path
from . import views

app_name='crud'

urlpatterns = [
    path('',views.task_list_and_create,name='crud_list'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    
    
]