from django.forms import ModelForm
from .models import  ToDo, User

class AddForm(ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'

class AddUser(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
