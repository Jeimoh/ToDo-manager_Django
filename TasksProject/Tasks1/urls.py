from django.urls import path
from . import views

app_name ='Tasks1'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('addTask/', views.addTask, name = 'addTask'),
]