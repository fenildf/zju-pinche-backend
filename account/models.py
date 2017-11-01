from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickName=models.CharField(max_length=20)
    gender=models.CharField(max_length=1,null=True,blank=True,default=None) #'M'|'F'
    phone=models.CharField(max_length=20,null=True,blank=True,default=None)
    weChat=models.CharField(max_length=30,null=True,blank=True,default=None)
    def dict(self):
        return {
            'joinedAt':self.date_joined.timestamp()*1000,
            'nickName':self.nickName,
            'gender':self.gender
        }
    def __str__(self):
        return self.username+self.nickName
