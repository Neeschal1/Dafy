from django.db import models
from .choices import *
from django.contrib.auth.models import User

class Payment(models.Model):
    Buyers_Name = models.ForeignKey(User, on_delete=models.CASCADE)
    Buyers_Username = models.CharField(max_length=30)
    Product_Name = models.CharField(max_length=30)
    Product_Description = models.TextField()
    Product_Image = models.URLField()
    Product_Category = models.CharField(max_length=3)
    Price = models.PositiveIntegerField()
    Paid = models.BooleanField(default=True)
    Payment_Time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.Buyers_Name}: {self.Product_Name}"