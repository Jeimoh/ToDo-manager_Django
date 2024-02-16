from django.shortcuts import render
from django.http import HttpResponse 
from django import forms
from .models import *


class addForm(forms.Form):
    Task = forms.CharField(label="New Task")


Created = ToDo.DateCreated
# Create your views here
def index(request):
    context = {'Tasks': ToDo.Title}
    return render(request, 'Tasks1/index.html', context)


def addTask(request):
    if (request.method == 'POST'):
        form = addForm(request.POST)
        if form.is_valid():
            Task = form.cleaned_data['Task']
            ToDo.append(Task)
    context = {'form': addForm(), 'Created':Created}
    return render(request, 'Tasks1/addTask.html', context)


