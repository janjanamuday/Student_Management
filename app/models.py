from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50,blank=False,null=False)
