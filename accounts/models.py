from django.db import models

# Create your models here.

class register(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField()
    password=models.CharField(max_length=100,)
    password2=models.CharField(max_length=100)


    