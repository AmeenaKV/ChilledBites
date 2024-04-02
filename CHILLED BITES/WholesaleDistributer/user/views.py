from django.shortcuts import render,redirect
from user.models import *
from site_admin.models import *
from datetime import date
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def registerAction(request):
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
    user=userregistration_tb(Name=Name,Address=Address,Phone_No=Phone_No,Email=Email,Gender=Gender,City=City,Pincode=Pincode,Proof=Proof,Username=Username,Password=Password,Confirm_password=Confirm_password)
    user.save()
    messages.add_message(request,messages.INFO,"Registered Successfully")
    return redirect('register')
def viewProduct(request):
    products=product_tb.objects.all()
    return render(request,'viewproduct.html',{'products':products})
def addtoCart(request,id):
    products=product_tb.objects.get(id=id)
    user=userregistration_tb.objects.get(id=request.session['id'])
    cart=cart_tb(ProductId=products,UserId=user,Count=1,Price=products.Price)
    cart.save()
    messages.add_message(request,messages.INFO,"Product Added to Cart Successfully")
    return redirect('viewProduct')
def viewCart(request):
    # userregistration_tb.objects.get(request.session['id'])
    vcart=cart_tb.objects.filter(UserId__id=request.session['id'])
    return render(request,'viewcart.html',{'vcart':vcart})
def deleteItem(request,id):
    cart=cart_tb.objects.get(id=id).delete()
    return redirect('viewCart')
def plusItem(request,id):
    cart=cart_tb.objects.get(id=id)
    if cart.ProductId_id:
        products=product_tb.objects.get(id=cart.ProductId_id)
        if cart.Count<products.Stock:
            cart.Count=int(cart.Count)+1
    else:
        products=productBaker_tb.objects.get(id=cart.BakerProductId_id)
        cart.Count=int(cart.Count)+1
    cart.Price=int(products.Price)*int(cart.Count)
    cart.save()
    return redirect('viewCart')
def minusItem(request,id):
    cart=cart_tb.objects.get(id=id)
    if cart.ProductId_id:
        products=product_tb.objects.get(id=cart.ProductId_id)
    else:
        products=productBaker_tb.objects.get(id=cart.BakerProductId_id)
    
    if int(cart.Count)>1:
        cart.Count=int(cart.Count)-1
        cart.Price=int(products.Price)*int(cart.Count)
        cart.save()
    return redirect('viewCart')
def viewBakerProductUser(request):
    products=productBaker_tb.objects.all()
    return render(request,'viewbakerproduct_user.html',{'products':products})
def addtoCartBaker(request,id):
    products=productBaker_tb.objects.get(id=id)
    user=userregistration_tb.objects.get(id=request.session['id'])
    cart=cart_tb(BakerProductId_id=products.id,UserId=user,Count=1,Price=products.AdminPrice)
    cart.save()
    messages.add_message(request,messages.INFO,"Product Added to Cart Successfully")
    return redirect('viewBakerProductUser')
def changePasswordUser(request):
    user=request.session['id']
    users=userregistration_tb.objects.filter(id=user)
    return render(request,"changepassworduser.html")
def changePasswordUserAction(request):
    user1=request.session['id']
    oldpassword=request.POST['OldPassword']
    newpassword=request.POST['NewPassword']
    confirmpassword=request.POST['ConfirmPassword']
    user2=userregistration_tb.objects.filter(id=user1,Password=oldpassword)
    if user2.count()>0:
        if newpassword==confirmpassword:
            userr=userregistration_tb.objects.filter(id=user1).update(Password=newpassword,Confirm_password=newpassword)
            messages.add_message(request,messages.INFO,"Updated Successfully")
        else:
            messages.add_message(request,messages.INFO,"Password is not equal")
    else:
        messages.add_message(request,messages.INFO,"Enter the current password correctly")
    return redirect('changePasswordUser')
def orderSummary(request):
    vcart=cart_tb.objects.filter(UserId__id=request.session['id'])
    grandTotal=0
    for item in vcart:
        grandTotal=grandTotal+int(item.Price)
    user=userregistration_tb.objects.filter(id=request.session['id'])
    return render(request,"orderdetails.html",{'user':user,'vcart':vcart,'gt':grandTotal})
def orderDetails(request):
    Name=request.POST['Name']
    Address=request.POST['Address']
    Phone_No=request.POST['Phone_No']
    Email=request.POST['Email']
    City=request.POST['City']
    Pincode=request.POST['Pincode']
    GrandTotal=request.POST['GrandTotal']
    deliveryType=request.POST['deliveryType']
    UserId=request.session['id']
    Date=date.today()
    order=order_tb(Name=Name,Address=Address,Phone_No=Phone_No,Email=Email,City=City,Pincode=Pincode,GrandTotal=GrandTotal,UserId_id=UserId,Date=Date,PaymentMode=deliveryType)
    order.save()
    vcart=cart_tb.objects.filter(UserId__id=request.session['id'])
    for item in vcart:
        if item.ProductId_id:
            orderItems=orderItem_tb(ProductId_id=item.ProductId_id,Oid_id=order.id,Quantity=item.Count,Price=item.Price)
            product=product_tb.objects.get(id=item.ProductId_id)
            Stock=int(product.Stock)-int(item.Count)
            product.Stock=Stock
            product.save()
        else:
            orderItems=orderItem_tb(BakerProductId_id=item.BakerProductId_id,Oid_id=order.id,Quantity=item.Count,Price=item.Price)
        orderItems.save()
    vcart=cart_tb.objects.filter(UserId__id=request.session['id']).delete()
    orders=order_tb.objects.filter(id=order.id)
    if deliveryType == 'card':
        return render(request,'paymentgateway.html',{'orders':orders})
    else:
        messages.add_message(request,messages.INFO,"Order Placed Successfully...")
        return redirect('viewMyOrder')
def viewMyOrder(request):
    user=request.session['id']
    orders=order_tb.objects.filter(UserId=user)
    return render(request,'viewmyorder.html',{'orders':orders})
def myorderdtls(request,id):
    orders=order_tb.objects.filter(id=id)
    orderitems=orderItem_tb.objects.filter(Oid_id=id)
    Status=tracking_tb.objects.filter(Oid=id)
    return render(request,'myorderdtls.html',{'orders':orders,'items':orderitems,'tracking':Status})
def viewStatusUser(request):
    track=tracking_tb(Oid=Oid,Status=Status,Date=Date)
    return redirect('viewMyOrder')
def apfeedback(request,id):
    return render(request,'apfeedback.html',{'id':id})
def adminProductFeedbackAction(request):
    UserId=request.session['id']
    Description=request.POST['Description']
    Id=request.POST['id']
    des=feedback_tb(Description=Description,ProductId_id=Id,UserId_id=UserId)
    des.save()
    messages.add_message(request,messages.INFO,"Feedback send successfully")
    return redirect('viewMyOrder')
def bpfeedback(request,id):
    return render(request,'bpfeedback.html',{'id':id})
def bakerProductFeedbackAction(request):
    UserId=request.session['id']
    Description=request.POST['Description']
    Id=request.POST['id']
    des=feedback_tb(Description=Description,BakerProductId_id=Id,UserId_id=UserId)
    des.save()
    messages.add_message(request,messages.INFO,"Feedback send successfully")
    return redirect('viewMyOrder')
def viewAdminFeedbackUser(request,id):
    userfeedback=feedback_tb.objects.filter(ProductId_id=id)
    return render(request,'viewfeedback.html',{'userfeedback':userfeedback})
def viewBakerFeedbackUser(request,id):
    userfeedback=feedback_tb.objects.filter(BakerProductId_id=id)
    return render(request,'viewfeedback.html',{'userfeedback':userfeedback})
def userPaymentAction(request):
    UserId=request.session['id']
    Oid=request.POST['Oid']
    NameonCard=request.POST['cardname']
    CreditCardNumber=request.POST['cardnumber']
    ExpDate=request.POST['expdate']
    CVV=request.POST['cvv']
    Amount=request.POST['GrandTotal']
    Pay=payment_tb(UserId_id=UserId,Oid_id=Oid,NameonCard=NameonCard,CreditCardNumber=CreditCardNumber,ExpDate=ExpDate,CVV=CVV,Amount=Amount)
    Pay.save()
    messages.add_message(request,messages.INFO,"Paid")
    return redirect('viewMyOrder')
def cancelorder(request,id):
    order=order_tb.objects.filter(id=id).update(Status="Cancelled")
    return redirect('viewMyOrder')
