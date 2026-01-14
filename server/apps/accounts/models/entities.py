from django.db import models
from .choices import *
from django.contrib.auth.models import User

class Userprofile(models.Model):
    Username = models.OneToOneField(User, on_delete=models.CASCADE)
    Full_Name = User.first_name
    Profile_Picture = models.URLField(default="https://i.pinimg.com/1200x/6e/59/95/6e599501252c23bcf02658617b29c894.jpg")
    Country_Code = models.CharField(max_length=5, default="+977")
    Phone_Number = models.CharField(max_length=10, default="9800000000")
    Address = models.TextField()
    def __str__(self):
        return self.Full_Name