from django.db import models

# Create your models here.


class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    FirstNames = models.CharField(max_length = 50)
    LastNames = models.CharField(max_length = 50)
    Email = models.EmailField()
    DateOB= models.DateField()
    def __str__ (self):
        return f"{self.UserId}"

class ToDo(models.Model):
    #ToDoId = models.AutoField(primary_key = True)
    Title = models.CharField(max_length = 200)
    DateCreated = models.DateTimeField(auto_now_add = True)
    DateUpdated = models.DateTimeField(auto_now= True)
    Creator = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__ (self):
       return self.Title
