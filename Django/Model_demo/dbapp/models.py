from django.db import models

# Create your models here.
class Employee(models.Model):
    empno=models.IntegerField()
    empname=models.CharField(max_length=20)
    empsalary=models.IntegerField()
    address=models.CharField(max_length=50)
