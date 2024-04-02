from django.db import models
class homebakerregistration_tb(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=30)
    Phone_No=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    Pincode=models.CharField(max_length=20)
    Proof=models.FileField(default="")
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    Confirm_password=models.CharField(max_length=20)
    Status=models.CharField(max_length=20,default="pending")
class productBaker_tb(models.Model):
    Image=models.FileField()
    Name=models.CharField(max_length=20)
    Price=models.CharField(max_length=20)
    Description=models.CharField(max_length=200,default="")
    AdminPrice=models.CharField(max_length=20,default="")
    BakerProductId=models.ForeignKey(homebakerregistration_tb,on_delete=models.CASCADE,null=True)
# Create your models here.
