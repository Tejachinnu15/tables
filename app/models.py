from django.db import models

# Create your models here.
class DEPT(models.Model):
    DNO=models.IntegerField(max_length=100,primary_key=True)
    DNAME=models.CharField(max_length=100)
    DLOC=models.CharField(max_length=100)
class EMP(models.Model):
    ENO=models.IntegerField(max_length=100)
    ENAME=models.CharField(max_length=100)
    EJOB=models.CharField(max_length=100)
    DNO=models.ForeignKey(DEPT,on_delete=models.CASCADE)