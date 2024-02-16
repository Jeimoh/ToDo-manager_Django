from django.db import models

# Create your models here.

class ToDo(models.Model):
    Title = models.Charfield(max_length = 200)
    DateCreated = 
