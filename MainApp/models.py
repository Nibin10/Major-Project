from django.db import models

# Create your models here.
class Userinfo(models.Model):
    username=models.CharField(max_length=30)
    emailid=models.CharField(max_length=50)
    password=models.CharField(max_length=30)

class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    image=models.ImageField(upload_to='bookimage/')
    audio=models.FileField(upload_to='audio/')