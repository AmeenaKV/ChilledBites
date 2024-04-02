from django.shortcuts import render,redirect
from staff.models import *
from user.models import *
from datetime import date
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def staffRegister(request):
    return render(request,'staff_register.html')
def staffRegisterAction(request):
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
    staff=staffregister_tb(Name=Name,Address=Address,Phone_No=Phone_No,Email=Email,Gender=Gender,City=City,Pincode=Pincode,Proof=Proof,Username=Username,Password=Password,Confirm_password=Confirm_password)
    staff.save()
    messages.add_message(request,messages.INFO,"Registered Successfully")
    return redirect('staffRegister')
def viewOrderByStaff(request):
    orders=order_tb.objects.all()
    return render(request,'vieworder_staff.html',{'orders':orders})
def orderDetailsActionStaff(request,id):
    orders=order_tb.objects.filter(id=id)
    orderitems=orderItem_tb.objects.filter(Oid=id)
    Status=tracking_tb.objects.filter(Oid=id)
    return render(request,'vieworderdetails_staff.html',{'orders':orders,'items':orderitems,'tracking':Status})
def viewStatusStaff(request):
    track=tracking_tb(Oid=Oid,Status=Status,Date=Date)
    return redirect('viewOrderByStaff')
def changePasswordStaff(request):
    staff=request.session['id']
    staffs=staffregister_tb.objects.filter(id=staff)
    return render(request,"changepasswordstaff.html")
def changePasswordStaffAction(request):
    staff1=request.session['id']
    oldpassword=request.POST['OldPassword']
    newpassword=request.POST['NewPassword']
    confirmpassword=request.POST['ConfirmPassword']
    stafff=staffregister_tb.objects.filter(id=staff1,Password=oldpassword)
    if stafff.count()>0:
        if newpassword==confirmpassword:
            staff=staffregister_tb.objects.filter(id=staff1).update(Password=newpassword,Confirm_password=newpassword)
            messages.add_message(request,messages.INFO,"Updated Successfully")
        else:
            messages.add_message(request,messages.INFO,"Password is not equal")
    else:
        messages.add_message(request,messages.INFO,"Enter the current password correctly")
    return redirect('changePasswordStaff')
def markdeliveredstaff(request,id):
    order=order_tb.objects.filter(id=id).update(Status="Delivered")
    return redirect('viewOrderByStaff')