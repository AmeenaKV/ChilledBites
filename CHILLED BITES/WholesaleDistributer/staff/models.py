from django.db import models

# Create your models here.
class staffregister_tb(models.Model):
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