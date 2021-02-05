from django.db import models

# Create your models here.
class user2(models.Model):
    id=models.IntegerField(primary_key=True)
    uname=models.CharField(max_length=20)
    password=models.CharField(max_length=25)
    email=models.CharField(max_length=50)
class user3(models.Model):
    id=models.IntegerField(primary_key=True)
    uname=models.CharField(max_length=20)
    password=models.CharField(max_length=25)
    email=models.CharField(max_length=50)