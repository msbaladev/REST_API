from django.db import models

# Create your models here.


# Create your models here.
class ProductData(models.Model):
    productName= models.CharField(max_length=254,null=False)
    image= models.CharField(max_length=254,null=False)
    price=models.CharField(max_length=255,null=False)
    
    
    
    
    
class products(models.Model):
    name= models.CharField(max_length=254,null=False)
    image= models.CharField(max_length=254,null=False)
    price=models.CharField(max_length=255,null=False)
    quantity=models.CharField(max_length=255,null=False)
    
    
    
class icc(models.Model):
    category= models.CharField(max_length=254,null=False)
    qpn= models.CharField(max_length=254,null=False)
    part_no= models.CharField(max_length=254,null=False)