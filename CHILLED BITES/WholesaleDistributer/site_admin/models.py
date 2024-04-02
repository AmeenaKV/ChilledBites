from django.db import models
# Create your models here.
class Admin_tb(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    Name=models.CharField(max_length=20,default='')
    Phone_No=models.CharField(max_length=20,default='')
class product_tb(models.Model):
    Image=models.FileField()
    Name=models.CharField(max_length=20)
    Price=models.CharField(max_length=20)
    Type=models.CharField(max_length=20)
    Flavour=models.CharField(max_length=20)
    Description=models.CharField(max_length=200,default="")
    Stock=models.CharField(max_length=20,default="")
class tracking_tb(models.Model):
    Oid=models.CharField(max_length=20)
    Date=models.DateField()
    Status=models.CharField(max_length=20,default="pending")
class adminpayment_tb(models.Model):
    bakerId=models.ForeignKey("homebaker.homebakerregistration_tb",on_delete=models.CASCADE,null=True)
    Oid=models.ForeignKey("user.order_tb",on_delete=models.CASCADE,null=True)
    NameonCard=models.CharField(max_length=20)
    CreditCardNumber=models.CharField(max_length=20)
    CVV=models.CharField(max_length=20)
    ExpDate=models.CharField(max_length=20)
    Amount=models.CharField(max_length=20)
class refundpayment_tb(models.Model):
    userId=models.ForeignKey("user.userregistration_tb",on_delete=models.CASCADE,null=True)
    Oid=models.ForeignKey("user.order_tb",on_delete=models.CASCADE,null=True)
    NameonCard=models.CharField(max_length=20)
    CreditCardNumber=models.CharField(max_length=20)
    CVV=models.CharField(max_length=20)
    ExpDate=models.CharField(max_length=20)
    Amount=models.CharField(max_length=20)