from django.shortcuts import render,redirect
from site_admin.models import *
from homebaker.models import *
from user.models import *
from staff.models import *
from datetime import date
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request,'login.html')
def loginAction(request):
    username=request.POST['Username']
    password=request.POST['Password']
    admin=Admin_tb.objects.filter(Username=username,Password=password)
    baker=homebakerregistration_tb.objects.filter(Username=username,Password=password)
    user=userregistration_tb.objects.filter(Username=username,Password=password)
    staff=staffregister_tb.objects.filter(Username=username,Password=password)
    if admin.count()>0:
        request.session['id']=admin[0].id
        return redirect('adminhome')
    elif baker.count()>0:
        status=baker[0].Status
        if status=="Approved":
            request.session['id']=baker[0].id
            return redirect('bakerhome')
        else:
            messages.add_message(request,messages.INFO,"Pending for Approval")
            return render(request,"login.html")
    elif user.count()>0:
        status=user[0].Status
        if status=="Approved":
            request.session['id']=user[0].id
            return redirect('userhome')
        else:
            messages.add_message(request,messages.INFO,"Pending for Approval")
            return render(request,"login.html")
    elif staff.count()>0:
        status=staff[0].Status
        if status=="Approved":
            request.session['id']=staff[0].id
            return redirect('staffhome')
        else:
            messages.add_message(request,messages.INFO,"Pending for Approval")
            return render(request,"login.html")
    else:
        messages.add_message(request,messages.INFO,"Incorrect Username or Password")
        return render(request,"login.html")
def adminhome(request):
    return render(request,'adminhome.html')
def bakerhome(request):
    return render(request,'bakerhome.html')
def staffhome(request):
    return render(request,'staffhome.html')
def userhome(request):
    return render(request,'userhome.html')
def aboutUs(request):
    return render(request,'about.html')
def contactUs(request):
    return render(request,'contact.html')
def approveBaker(request):
    baker=homebakerregistration_tb.objects.filter(Status="pending")
    return render(request,"viewhomebaker.html",{'baker':baker})
def detailsbaker(request,id):
    det=homebakerregistration_tb.objects.filter(id=id)
    return render(request,"detailbaker.html",{'baker':det})
def approveb(request,id):
    app=homebakerregistration_tb.objects.filter(id=id).update(Status="Approved")
    return redirect('approveBaker')
def rejectb(request,id):
    rej=homebakerregistration_tb.objects.filter(id=id).update(Status="Rejected")
    return redirect('approveBaker')
def approvedBaker(request):
    v=homebakerregistration_tb.objects.all()
    return render(request,'viewapprovedbaker.html',{'baker':v})
def deleteBaker(request,id):
    db=homebakerregistration_tb.objects.filter(id=id).delete()
    return redirect('approvedBaker')
def addProduct(request):
    return render(request,"add_product.html")
def addProductAction(request):
    productName=request.POST['pname']
    description=request.POST['description']
    price=request.POST['price']
    type=request.POST['type']
    flavour=request.POST['flavour']
    stock=request.POST['stock']
    image=""
    if len(request.FILES)>0:
        image=request.FILES["image"]
    else:
        image="No Pic"
    product=product_tb(Name=productName,Price=price,Type=type,Flavour=flavour,Description=description,Stock=stock,Image=image)
    product.save()
    messages.add_message(request,messages.INFO,"Product Added Successfully")
    return render(request,"add_product.html")
def approveUser(request):
    user=userregistration_tb.objects.filter(Status="pending")
    return render(request,"viewuser.html",{'user':user})
def detailuser(request,id):
    det=userregistration_tb.objects.filter(id=id)
    return render(request,"detailuser.html",{'user':det})
def approveu(request,id):
    app=userregistration_tb.objects.filter(id=id).update(Status="Approved")
    return redirect('approveUser')
def rejectu(request,id):
    rej=userregistration_tb.objects.filter(id=id).update(Status="Rejected")
    return redirect('approveUser')
def approvedUser(request):
    v=userregistration_tb.objects.all()
    return render(request,'viewapproveduser.html',{'user':v})
def deleteUser(request,id):
    du=userregistration_tb.objects.filter(id=id).delete()
    return redirect('approvedUser')
def viewProductAdmin(request):
    products=product_tb.objects.all()
    return render(request,'viewproduct_admin.html',{'products':products})
def adminEdit(request,id):
    #admin=request.session['id']
    admin1=product_tb.objects.filter(id=id)
    return render(request,"adminedit.html",{'admin':admin1})
def adminEditAction(request):
    admins=request.POST['id']
    product=product_tb.objects.filter(id=admins)
    if(len(request.FILES)>0):
        img=request.FILES['file']
    else:
        img=product[0].Image
    name=request.POST['pname']
    des=request.POST['description']
    price=request.POST['price']
    types=request.POST['type']
    flavour=request.POST['flavour']
    stock=request.POST['stock']
    ap=product_tb.objects.filter(id=admins).update(Name=name,Description=des,Price=price,Type=types,Flavour=flavour,Stock=stock)
    product_object=product_tb.objects.get(id=admins)
    product_object.Image=img
    product_object.save()
    messages.add_message(request,messages.INFO,"Product Edited Successfully")
    return redirect("viewProductAdmin")
def deleteProductAdmin(request,id):
    dp=product_tb.objects.get(id=id).delete()
    return redirect('viewProductAdmin')
def viewBakerProduct(request):
    products=productBaker_tb.objects.all()
    return render(request,'viewbakerproduct_admin.html',{'products':products})
def forgotPassword(request):
    return render(request,"forgotpassword.html")
def forgotPasswordAction(request):
    username=request.POST['Username']
    admin=Admin_tb.objects.filter(Username=username)
    baker=homebakerregistration_tb.objects.filter(Username=username)
    user=userregistration_tb.objects.filter(Username=username)
    staff=staffregister_tb.objects.filter(Username=username)
    if admin.count()>0:
        return render(request,"newpassword.html",{'data':username})
    elif baker.count()>0:
        return render(request,"newpassword.html",{'data':username})
    elif user.count()>0:
        return render(request,"newpassword.html",{'data':username})
    elif staff.count()>0:
        return render(request,"newpassword.html",{'data':username})
    else:
        messages.add_message(request,messages.INFO,"Invalid username")
        return redirect("forgotPassword")
def viewBakerProductAction(request):
    pid=request.POST['pid']
    adminPrice=request.POST['adminPrice']
    apb=productBaker_tb.objects.filter(id=pid).update(AdminPrice=adminPrice)
    return redirect('viewBakerProduct')
def newPasswordAction(request):
    username=request.POST['Username']
    name=request.POST['Name']
    phoneno=request.POST['Phone_No']
    admins=Admin_tb.objects.filter(Username=username,Name=name,Phone_No=phoneno)
    bakers=homebakerregistration_tb.objects.filter(Username=username,Name=name,Phone_No=phoneno)
    users=userregistration_tb.objects.filter(Username=username,Name=name,Phone_No=phoneno)
    staffs=staffregister_tb.objects.filter(Username=username,Name=name,Phone_No=phoneno)
    if admins.count()>0:
        return render(request,"enternewpswd.html",{'data':username})
    elif  bakers.count()>0:
        return render(request,"enternewpswd.html",{'data':username})
    elif users.count()>0:
        return render(request,"enternewpswd.html",{'data':username})
    elif staffs.count()>0:
        return render(request,"enternewpswd.html",{'data':username})
    else:
        messages.add_message(request,messages.INFO,"Invalid credential")
        return render(request,"newpassword.html",{'data':username})
def enterNewPasswordAction(request):
    username=request.POST['Username']
    newPassword=request.POST['NewPassword']
    confirm_newPassword=request.POST['Confirm_NewPassword']
    if newPassword==confirm_newPassword: 
        admin=Admin_tb.objects.filter(Username=username)
        baker=homebakerregistration_tb.objects.filter(Username=username)
        user=userregistration_tb.objects.filter(Username=username)
        staff=staffregister_tb.objects.filter(Username=username)
        if admin.count()>0:
            request.session['id']=admin[0].id
            adminid=request.session['id']
            admin=Admin_tb.objects.filter(id=adminid).update(Password=newPassword)
        elif baker.count()>0:
            request.session['id']=baker[0].id
            bakerid=request.session['id']
            baker=homebakerregistration_tb.objects.filter(id=bakerid).update(Password=newPassword,Confirm_password=confirm_newPassword)
        elif user.count()>0:
            request.session['id']=user[0].id
            userid=request.session['id']
            user=userregistration_tb.objects.filter(id=userid).update(Password=newPassword,Confirm_password=confirm_newPassword)
        else:
            request.session['id']=staff[0].id
            staffid=request.session['id']
            staff=staffregister_tb.objects.filter(id=staffid).update(Password=newPassword,Confirm_password=confirm_newPassword)
        messages.add_message(request,messages.INFO,"Password changed successfully")
        request.session.flush()
        return redirect("login")
    else:
        messages.add_message(request,messages.INFO,"Password doesn't match")
        return render(request,"enternewpswd.html",{"data":username})
def changePasswordAdmin(request):
    admin=request.session['id']
    ad=Admin_tb.objects.filter(id=admin)
    return render(request,"changepasswordadmin.html")
def changePasswordAdminAction(request):
    adm=request.session['id']
    oldpassword=request.POST['OldPassword']
    newpassword=request.POST['NewPassword']
    confirmpassword=request.POST['ConfirmPassword']
    admn=Admin_tb.objects.filter(id=adm,Password=oldpassword)
    if admn.count()>0:
        if newpassword==confirmpassword:
            admin=Admin_tb.objects.filter(id=adm).update(Password=newpassword)
            messages.add_message(request,messages.INFO,"Updated Successfully")
        else:
            messages.add_message(request,messages.INFO,"Password is not equal")
    else:
        messages.add_message(request,messages.INFO,"Enter the current password correctly")
    return redirect('changePasswordAdmin')
def viewOrderByAdmin(request):
    orders=order_tb.objects.all()
    return render(request,'vieworder_admin.html',{'orders':orders})
def orderDetailsAction(request,id):
    orders=order_tb.objects.filter(id=id)
    orderitems=orderItem_tb.objects.filter(Oid=id)
    Status=tracking_tb.objects.filter(Oid=id)
    return render(request,'vieworderdetails_admin.html',{'orders':orders,'items':orderitems,'tracking':Status})
def addStatusAdmin(request):
    Oid=request.POST['Oid'] 
    Status=request.POST['Status'] 
    Date=date.today()
    track=tracking_tb(Oid=Oid,Status=Status,Date=Date)
    track.save()
    messages.add_message(request,messages.INFO,"Status Added Successfully")
    return redirect('viewOrderByAdmin')
def approveStaff(request):
    staff=staffregister_tb.objects.filter(Status="pending")
    return render(request,"viewstaff.html",{'staff':staff})
def detailstaff(request,id):
    det=staffregister_tb.objects.filter(id=id)
    return render(request,"detailstaff.html",{'staff':det})
def approves(request,id):
    app=staffregister_tb.objects.filter(id=id).update(Status="Approved")
    return redirect('approveStaff')
def rejects(request,id):
    rej=staffregister_tb.objects.filter(id=id).update(Status="Rejected")
    return redirect('approveStaff')
def approvedStaff(request):
    v=staffregister_tb.objects.all()
    return render(request,'viewapprovedstaff.html',{'staff':v})
def deleteStaff(request,id):
    ds=staffregister_tb.objects.filter(id=id).delete()
    return redirect('approvedStaff')
def logout(request):
    request.session.flush()
    return redirect('index')
def viewFeedbackAdmin(request,id):
    userfeedback=feedback_tb.objects.filter(ProductId_id=id)
    return render(request,'viewfeedback.html',{'userfeedback':userfeedback})
def viewBakerOrderByAdmin(request):
    orderitems=orderItem_tb.objects.all().select_related('Oid').values('Oid_id')
    orders=order_tb.objects.filter(id__in=orderitems)
    bakers=homebakerregistration_tb.objects.all()
    return render(request,'viewbakerorder_admin.html',{'orders':orders,'bakers':bakers})
def viewBakersOrder(request):
    bakerProduct=productBaker_tb.objects.filter(BakerProductId_id=request.GET['bakerid']).values('id')
    orderitems=orderItem_tb.objects.filter(BakerProductId_id__in=bakerProduct).select_related('Oid').values('Oid_id')
    orders=order_tb.objects.filter(id__in=orderitems)
    return render(request,'viewbakerorder_result.html',{'orders':orders})
def bakerOrderDetailsActionAdmin(request,id,bid):
    bakerProduct=productBaker_tb.objects.filter(BakerProductId_id=bid).values('id')
    orderitems=orderItem_tb.objects.filter(Oid=id,ProductId_id__isnull=True,BakerProductId_id__in=bakerProduct).select_related('Oid')
    orders=order_tb.objects.filter(id=id)
    # orderitems=orderItem_tb.objects.filter(Oid=id,ProductId_id__isnull=True)
    Status=tracking_tb.objects.filter(Oid=id)
    bamount=0
    for i in orderitems:
        bamount=bamount+int(i.BakerProductId.Price)
    # orderitems[0].BakerProductId.BakerProductId.id
    return render(request,'viewbakerorderdetails_admin.html',{'orders':orders,'items':orderitems,'tracking':Status,"bakerAmount":bamount,"bakerId":bid})
def adminPayment(request,price,bid,oid):
    return render(request,'paymentadmin.html',{'Price':price,'bakerId':bid,'Oid':oid})
def adminPaymentAction(request):
    bakerId=request.POST['bakerId']
    Oid=request.POST['Oid']
    NameonCard=request.POST['cardname']
    CreditCardNumber=request.POST['cardnumber']
    ExpDate=request.POST['expdate']
    CVV=request.POST['cvv']
    Amount=request.POST['Price']
    Pay=adminpayment_tb(NameonCard=NameonCard,CreditCardNumber=CreditCardNumber,ExpDate=ExpDate,CVV=CVV,Amount=Amount,bakerId_id=bakerId,Oid_id=Oid)
    Pay.save()
    order=order_tb.objects.filter(id=Oid).update(Status="Paid")
    messages.add_message(request,messages.INFO,"Paid")
    return redirect('viewBakerOrderByAdmin')
def refundPayment(request,price,uid,oid):
    return render(request,'refundpaymentadmin.html',{'Price':price,'userId':uid,'Oid':oid})
def refundPaymentAction(request):
    userId=request.POST['userId']
    Oid=request.POST['Oid']
    NameonCard=request.POST['cardname']
    CreditCardNumber=request.POST['cardnumber']
    ExpDate=request.POST['expdate']
    CVV=request.POST['cvv']
    Amount=request.POST['Price']
    Pay=refundpayment_tb(NameonCard=NameonCard,CreditCardNumber=CreditCardNumber,ExpDate=ExpDate,CVV=CVV,Amount=Amount,userId_id=userId,Oid_id=Oid)
    Pay.save()
    order=order_tb.objects.filter(id=Oid).update(Status="Refunded")
    messages.add_message(request,messages.INFO,"Refunded Successfully...")
    return redirect('viewOrderByAdmin')
# def markdelivered(request,id):
#     order=order_tb.objects.filter(id=id).update(Status="Delivered")
#     return redirect('viewOrderByAdmin')