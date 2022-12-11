from django.db import models

# Create your models here.

class Vendoradd(models.Model):
    vendorname=models.CharField(max_length=100)
    vendoraddress=models.CharField(max_length=200)
    vednorcontactno=models.IntegerField()
    vendoremail=models.EmailField()
    vendorimage=models.ImageField(blank=True,upload_to='vendorimages')
    vendorgistn=models.CharField(max_length=50)