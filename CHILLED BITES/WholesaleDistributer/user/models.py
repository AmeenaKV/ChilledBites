from django.db import models
from site_admin.models import *
from homebaker.models import *
class userregistration_tb(models.Model):
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
class cart_tb(models.Model):
    ProductId=models.ForeignKey(product_tb,on_delete=models.CASCADE,null=True)
    UserId=models.ForeignKey(userregistration_tb,on_delete=models.CASCADE,default='0')
    Count=models.CharField(max_length=20)
    Price=models.CharField(max_length=20)
    BakerProductId=models.ForeignKey(productBaker_tb,on_delete=models.CASCADE,null=True)
class order_tb(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=30)
    Phone_No=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    Pincode=models.CharField(max_length=20)
    UserId=models.ForeignKey(userregistration_tb,on_delete=models.CASCADE,null=True)
    GrandTotal=models.CharField(max_length=20)
    Date=models.DateField()
    Status=models.CharField(max_length=20,default="pending")
    PaymentMode=models.CharField(max_length=20,default='')
class orderItem_tb(models.Model):
    ProductId=models.ForeignKey(product_tb,on_delete=models.CASCADE,null=True)
    BakerProductId=models.ForeignKey(productBaker_tb,on_delete=models.CASCADE,null=True)
    Oid=models.ForeignKey(order_tb,on_delete=models.CASCADE,null=True)
    Quantity=models.CharField(max_length=20)
    Price=models.CharField(max_length=20,null=True)
class feedback_tb(models.Model):
    ProductId=models.ForeignKey(product_tb,on_delete=models.CASCADE,null=True)
    BakerProductId=models.ForeignKey(productBaker_tb,on_delete=models.CASCADE,null=True)
    Description=models.CharField(max_length=20)
    UserId=models.ForeignKey(userregistration_tb,on_delete=models.CASCADE,null=True)
class payment_tb(models.Model):
    UserId=models.ForeignKey(userregistration_tb,on_delete=models.CASCADE)
    Oid=models.ForeignKey(order_tb,on_delete=models.CASCADE)
    NameonCard=models.CharField(max_length=20)
    CreditCardNumber=models.CharField(max_length=20)
    CVV=models.CharField(max_length=20)
    ExpDate=models.CharField(max_length=20)
    Amount=models.CharField(max_length=20)
# Create your models here.
