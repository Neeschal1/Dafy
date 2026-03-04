from django.db import models
from django.contrib.auth.models import User
from .choices import *

class Product(models.Model):
    Product_Name = models.CharField(max_length=40)
    Product_ID = models.CharField(max_length=10)
    Product_Category = models.CharField(max_length=3, choices=PRODUCT_CATEGORY_CHOICES)
    Product_Description = models.TextField()
    Image_one = models.URLField(blank=False)
    Image_two = models.URLField(blank=False)
    Image_three = models.URLField(blank=False)
    Image_four = models.URLField()
    Image_five = models.URLField()
    Seller_Name = models.ForeignKey(User, on_delete=models.CASCADE)
    Seller_Address = models.TextField()
    Price = models.PositiveIntegerField(default=10)
    Bought_Date = models.DateTimeField()
    Created_Date = models.DateTimeField(auto_now_add=True)
    Updated_Date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.Product_Name} || {self.Product_ID}"