from django.urls import path
from . import views

app_name ='Tasks1'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('Tasks/<str:pk>/',views.Task, name = "ToDo"),
    path('addTask/', views.addTask, name = 'addTask'),
    path('login/', views.addUser, name = 'addUser'),
]