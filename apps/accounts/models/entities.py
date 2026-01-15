from django.db import models
from .choices import *
from django.contrib.auth.models import User

class Userprofile(models.Model):
    Username = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_Picture = models.URLField()
    Country_Code = models.CharField(max_length=30, default="+977", choices=COUNTRY_CODE_CHOICES)
    Phone_Number = models.CharField(max_length=10, default="9800000000")
    Address = models.TextField()
    def __str__(self):
        return self.Username.first_name