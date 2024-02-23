from django.urls import path
from . import views

app_name ='Tasks1'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('user/<int:user_id>/', views.user_tasks, name='user_tasks'),
    path('Tasks/<str:pk>/',views.Task, name = "ToDo"),
    path('addTask/', views.addTask, name = 'addTask'),
    path('addUser/', views.addUser, name = 'addUser'),
    
]