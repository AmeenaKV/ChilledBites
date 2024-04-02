from django.shortcuts import render,redirect
from homebaker.models import *
from user.models import *
from datetime import date
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def bakerRegister(request):
    return render(request,'homebaker_registration.html')
def bakerRegisterAction(request):
    Proof=""
    if len(request.FILES)>0:
        Proof=request.FILES["Proof"]
    else:
        Proof="No File"
    Name=request.POST['Name']
    Address=request.POST['Address']
    Phone_No=request.POST['Phone_No']
    Email=request.POST['Email']
    Gender=request.POST['Gender']
    City=request.POST['City']
    Pincode=request.POST['Pincode']
    Username=request.POST['Username']
    Password=request.POST['Password']
    Confirm_password=request.POST['Confirm_password']  
    homebaker=homebakerregistration_tb(Name=Name,Address=Address,Phone_No=Phone_No,Email=Email,Gender=Gender,City=City,Pincode=Pincode,Proof=Proof,Username=Username,Password=Password,Confirm_password=Confirm_password,Status="pending")
    homebaker.save()
    messages.add_message(request,messages.INFO,"Registered Successfully")
    return redirect('bakerRegister')
def addProductBaker(request):
    return render(request,"addproductbaker.html")
def addProductBakerAction(request):
    productName=request.POST['pname']
    description=request.POST['description']
    price=request.POST['price']
    image=""
    if len(request.FILES)>0:
        image=request.FILES["image"]
    else:
        image="No Pic"
    baker=homebakerregistration_tb.objects.get(id=request.session['id'])
    productBaker=productBaker_tb(Name=productName,Price=price,Description=description,Image=image,AdminPrice=price,BakerProductId=baker)
    productBaker.save()
    messages.add_message(request,messages.INFO,"Product Added Successfully")
    return render(request,"addproductbaker.html")
def viewProductBaker(request):
    products=productBaker_tb.objects.filter(BakerProductId_id=request.session['id'])
    return render(request,'viewproduct_baker.html',{'products':products})
def bakerEdit(request,id):
    # baker=request.session['id']
    baker=productBaker_tb.objects.filter(id=id)
    return render(request,"bakeredit.html",{'baker':baker})
def bakerEditAction(request):
    baker=request.POST['id']
    product=productBaker_tb.objects.filter(id=baker)
    if(len(request.FILES)>0):
        img=request.FILES['file']
    else:
        img=product[0].Image
    name=request.POST['pname']
    des=request.POST['description']
    price=request.POST['price']
    apb=productBaker_tb.objects.filter(id=baker).update(Name=name,Description=des,Price=price)
    product_object=productBaker_tb.objects.get(id=baker)
    product_object.Image=img
    product_object.save()
    messages.add_message(request,messages.INFO,"Product Edited Successfully")
    return redirect("viewProductBaker")
def deleteProductBaker(request,id):
    dpb=productBaker_tb.objects.get(id=id).delete()
    return redirect('viewProductBaker')
def changePasswordBaker(request):
    baker=request.session['id']
    bakers=homebakerregistration_tb.objects.filter(id=baker)
    return render(request,"changepasswordbaker.html")
def changePasswordBakerAction(request):
    baker1=request.session['id']
    oldpassword=request.POST['OldPassword']
    newpassword=request.POST['NewPassword']
    confirmpassword=request.POST['ConfirmPassword']
    bakery=homebakerregistration_tb.objects.filter(id=baker1,Password=oldpassword)
    if bakery.count()>0:
        if newpassword==confirmpassword:
            baker=homebakerregistration_tb.objects.filter(id=baker1).update(Password=newpassword,Confirm_password=newpassword)
            messages.add_message(request,messages.INFO,"Updated Successfully")
        else:
            messages.add_message(request,messages.INFO,"Password is not equal")
    else:
        messages.add_message(request,messages.INFO,"Enter the current password correctly")
    return redirect('changePasswordBaker')
def viewOrderByBaker(request):
    bakerProduct=productBaker_tb.objects.filter(BakerProductId_id=request.session['id']).values('id')
    orderitems=orderItem_tb.objects.filter(BakerProductId_id__in=bakerProduct).select_related('Oid').values('Oid_id')
    orders=order_tb.objects.filter(id__in=orderitems)
    return render(request,'vieworder_baker.html',{'orders':orders})
def orderDetailsActionBaker(request,id):
    bakerProduct=productBaker_tb.objects.filter(BakerProductId_id=request.session['id']).values('id')
    orderitems=orderItem_tb.objects.filter(Oid=id,ProductId_id__isnull=True,BakerProductId_id__in=bakerProduct).select_related('Oid')
    orders=order_tb.objects.filter(id=id)
    # orderitems=orderItem_tb.objects.filter(Oid=id,ProductId_id__isnull=True)
    Status=tracking_tb.objects.filter(Oid=id)
    return render(request,'vieworderdetails_baker.html',{'orders':orders,'items':orderitems,'tracking':Status})
def addStatusBaker(request):
    Oid=request.POST['Oid'] 
    Status=request.POST['Status']
    Date=date.today()
    track=tracking_tb(Oid=Oid,Status=Status,Date=Date)
    track.save()
    messages.add_message(request,messages.INFO,"Status Added Successfully")
    return redirect('viewOrderByBaker')
def viewFeedbackBaker(request,id):
    userfeedback=feedback_tb.objects.filter(BakerProductId_id=id)
    return render(request,'viewfeedback.html',{'userfeedback':userfeedback})
# def markdeliveredbaker(request,id):
#     order=order_tb.objects.filter(id=id).update(Status="Delivered")
#     return redirect('viewOrderByBaker')