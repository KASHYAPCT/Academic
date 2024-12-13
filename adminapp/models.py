from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    is_fac= models.BooleanField(default=False)
    is_stud = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=12,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    place= models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=30,null=True,blank=True)
    image = models.ImageField(upload_to="user/",null=True,blank=True)
    semester=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=150,null=True,blank=True)
    
    
    
# class Department(models.Model):
#     dep_id=models.ForeignKey(null=True,blank=True)
#     dep_name=models.CharField(max_length=50,null=True,blank=True)
  

    
    