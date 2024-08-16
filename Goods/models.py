from django.db import models 
from django.contrib.auth.models import User 
from random import sample 
import string 
 

 
 
class Category(models.Model): 
    name = models.CharField(max_length=255) 
    imges = models.ImageField() 
     
     
 
    def __str__(self): 
        return self.name 
 
    def save(self, *args, **kwargs): 
        if not self.generate_code: 
            self.generate_code = "".join(sample(string.ascii_letters, 20)) 
        super(Category, self).save(*args, **kwargs) 
 
class Product(models.Model): 
    name = models.CharField(max_length=255) 
    quantity = models.PositiveIntegerField(default=1) 
    price = models.DecimalField(max_digits=8, decimal_places=2) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    description = models.TextField() 
 
    def __str__(self): 
        return self.name 
     
    
        