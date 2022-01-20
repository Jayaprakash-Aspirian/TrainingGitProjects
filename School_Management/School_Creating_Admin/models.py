from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class MyUser(AbstractUser):
    joined_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["joined_date"]

    def __str__(self):
        return self.username

class school_details(models.Model):
    schoolname   = models.CharField(max_length=100)
    schooladdress= models.CharField( max_length=100)   
    schooldistrict= models.CharField( max_length=20)
    schoolstate=models.CharField(max_length=20,default="Tamilnadu")
    schoolcountry=models.CharField(max_length=20,default="India")
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE)

