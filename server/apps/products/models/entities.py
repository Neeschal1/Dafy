from django.db import models

class Product(models.Model):
    Prod_Image = models.ImageField()
    Prod_Name = models.CharField(max_length=30)
    Prod_Rate = models.IntegerField()
    
    def __str__(self):
        return self.Prod_Name