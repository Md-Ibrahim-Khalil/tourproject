from django.db import models

# Create your models here.
class Agency(models.Model):
    name = models.CharField(max_length=100)
    nid_number = models.CharField(max_length=13)
    phone_number = models.CharField(max_length=11)
    
    
class Tour(models.Model):
    package_name = models.CharField(max_length=100)
    package_price = models.DecimalField(max_digits=8, decimal_places=2)
    confirmed = models.BooleanField(default=False)

