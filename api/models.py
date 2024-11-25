from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=1)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
