from django.shortcuts import render
from django.http import HttpResponse 
from django import forms


class addForm(forms.Form):
    Task = forms.CharField(label="New Task")

Tasks = []
# Create your views here
def index(request):
    context = {'Tasks': Tasks}
    return render(request, 'Tasks1/index.html', context)


def addTask(request):
    if (request.method == 'POST'):
        form = addForm(request.POST)
        if form.is_valid():
            Task = form.cleaned_data['Task']
            Tasks.append(Task)
    context = {'form': addForm()}
    return render(request, 'Tasks1/addTask.html', context)


