"""WholesaleDistributer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from user import views as userviews
from homebaker import views as homebakerviews
from site_admin import views as site_adminviews
from staff import views as staffviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userviews.index,name="index"),
    path('adminhome',site_adminviews.adminhome,name="adminhome"),
    path('bakerhome',site_adminviews.bakerhome,name="bakerhome"),
    path('staffhome',site_adminviews.staffhome,name="staffhome"),
    path('aboutUs',site_adminviews.aboutUs,name="aboutUs"),
    path('contactUs',site_adminviews.contactUs,name="contactUs"),
    path('userhome',site_adminviews.userhome,name="userhome"),
    path('register/',userviews.register,name="register"),
    path('registerAction/',userviews.registerAction,name="registerAction"),
    path('bakerRegister/',homebakerviews.bakerRegister,name="bakerRegister"),
    path('bakerRegisterAction/',homebakerviews.bakerRegisterAction,name="bakerRegisterAction"),
    path('staffRegister/',staffviews.staffRegister,name="staffRegister"),
    path('staffRegisterAction/',staffviews.staffRegisterAction,name="staffRegisterAction"),
    path('login/',site_adminviews.login,name="login"),
    path('loginAction/',site_adminviews.loginAction,name="loginAction"),
    path('detailsbaker<int:id>/',site_adminviews.detailsbaker,name="detailsbaker"),
    path('approveb<int:id>/',site_adminviews.approveb,name="approveb"),
    path('rejectb<int:id>/',site_adminviews.rejectb,name="rejectb"),
    path('addProduct/',site_adminviews.addProduct,name="addProduct"),
    path('addProductAction/',site_adminviews.addProductAction,name="addProductAction"),
    path('viewProduct/',userviews.viewProduct,name="viewProduct"),
    path('approveBaker/',site_adminviews.approveBaker,name="approveBaker"), 
    path('approvedBaker/',site_adminviews.approvedBaker,name="approvedBaker"),
    path('deleteBaker<int:id>/',site_adminviews.deleteBaker,name="deleteBaker"),
    path('addtoCart<int:id>/',userviews.addtoCart,name="addtoCart"),
    path('viewCart/',userviews.viewCart,name="viewCart"),
    path('deleteItem<int:id>/',userviews.deleteItem,name="deleteItem"),
    path('minusItem<int:id>/',userviews.minusItem,name="minusItem"),
    path('plusItem<int:id>/',userviews.plusItem,name="plusItem"),
    path('detailuser<int:id>/',site_adminviews.detailuser,name="detailuser"),
    path('approveUser/',site_adminviews.approveUser,name="approveUser"),  
    path('approveu<int:id>/',site_adminviews.approveu,name="approveu"),
    path('rejectu<int:id>/',site_adminviews.rejectu,name="rejectu"),
    path('approvedUser/',site_adminviews.approvedUser,name="approvedUser"),
    path('deleteUser<int:id>/',site_adminviews.deleteUser,name="deleteUser"),
    path('adminEdit<int:id>/',site_adminviews.adminEdit,name="adminEdit"),
    path('adminEditAction/',site_adminviews.adminEditAction,name="adminEditAction"),
    path('viewProductAdmin/',site_adminviews.viewProductAdmin,name="viewProductAdmin"),
    path('deleteProductAdmin<int:id>/',site_adminviews.deleteProductAdmin,name="deleteProductAdmin"),
    path('addProductBaker/',homebakerviews.addProductBaker,name="addProductBaker"),
    path('addProductBakerAction/',homebakerviews.addProductBakerAction,name="addProductBakerAction"),
    path('viewProductBaker/',homebakerviews.viewProductBaker,name="viewProductBaker"),
    path('bakerEdit<int:id>/',homebakerviews.bakerEdit,name="bakerEdit"),
    path('bakerEditAction/',homebakerviews.bakerEditAction,name="bakerEditAction"),
    path('deleteProductBaker<int:id>/',homebakerviews.deleteProductBaker,name="deleteProductBaker"),
    path('viewBakerProduct/',site_adminviews.viewBakerProduct,name="viewBakerProduct"),
    path('forgotPassword/',site_adminviews.forgotPassword,name="forgotPassword"),
    path('forgotPasswordAction/',site_adminviews.forgotPasswordAction,name="forgotPasswordAction"),
    path('viewBakerProductAction/',site_adminviews.viewBakerProductAction,name="viewBakerProductAction"),
    path('newPasswordAction/',site_adminviews.newPasswordAction,name="newPasswordAction"),
    path('enterNewPasswordAction/',site_adminviews.enterNewPasswordAction,name="enterNewPasswordAction"),
    path('viewBakerProductUser/',userviews.viewBakerProductUser,name="viewBakerProductUser"),
    path('addtoCartBaker<int:id>/',userviews.addtoCartBaker,name="addtoCartBaker"),
    path('changePasswordBaker/',homebakerviews.changePasswordBaker,name="changePasswordBaker"),
    path('changePasswordBakerAction/',homebakerviews.changePasswordBakerAction,name="changePasswordBakerAction"),
    path('changePasswordUser/',userviews.changePasswordUser,name="changePasswordUser"),
    path('changePasswordUserAction/',userviews.changePasswordUserAction,name="changePasswordUserAction"),
    path('changePasswordAdmin/',site_adminviews.changePasswordAdmin,name="changePasswordAdmin"),
    path('changePasswordAdminAction/',site_adminviews.changePasswordAdminAction,name="changePasswordAdminAction"),
    path('orderSummary/',userviews.orderSummary,name="orderSummary"),
    path('orderDetails/',userviews.orderDetails,name="orderDetails"),
    path('viewMyOrder/',userviews.viewMyOrder,name="viewMyOrder"),
    path('myorderdtls/<int:id>',userviews.myorderdtls,name="myorderdtls"),
    path('viewOrderByAdmin/',site_adminviews.viewOrderByAdmin,name="viewOrderByAdmin"),
    path('orderDetailsAction/<int:id>',site_adminviews.orderDetailsAction,name="orderDetailsAction"),
    path('viewOrderByBaker/',homebakerviews.viewOrderByBaker,name="viewOrderByBaker"),
    path('orderDetailsActionBaker/<int:id>',homebakerviews.orderDetailsActionBaker,name="orderDetailsActionBaker"),
    path('addStatusAdmin/',site_adminviews.addStatusAdmin,name="addStatusAdmin"),
    path('addStatusBaker/',homebakerviews.addStatusBaker,name="addStatusBaker"),
    path('viewStatusUser/',userviews.viewStatusUser,name="viewStatusUser"),
    path('viewOrderByStaff/',staffviews.viewOrderByStaff,name="viewOrderByStaff"),
    path('orderDetailsActionStaff/<int:id>',staffviews.orderDetailsActionStaff,name="orderDetailsActionStaff"),
    path('viewStatusStaff/',staffviews.viewStatusStaff,name="viewStatusStaff"),
    path('detailstaff<int:id>/',site_adminviews.detailstaff,name="detailstaff"),
    path('approveStaff/',site_adminviews.approveStaff,name="approveStaff"),  
    path('approves<int:id>/',site_adminviews.approves,name="approves"),
    path('rejects<int:id>/',site_adminviews.rejects,name="rejects"),
    path('approvedStaff/',site_adminviews.approvedStaff,name="approvedStaff"),
    path('deleteStaff<int:id>/',site_adminviews.deleteStaff,name="deleteStaff"),
    path('changePasswordStaff/',staffviews.changePasswordStaff,name="changePasswordStaff"),
    path('changePasswordStaffAction/',staffviews.changePasswordStaffAction,name="changePasswordStaffAction"),
    path('apfeedback/<int:id>',userviews.apfeedback,name="apfeedback"),
    path('adminProductFeedbackAction/',userviews.adminProductFeedbackAction,name="adminProductFeedbackAction"),
    path('bpfeedback/<int:id>',userviews.bpfeedback,name="bpfeedback"),
    path('bakerProductFeedbackAction/',userviews.bakerProductFeedbackAction,name="bakerProductFeedbackAction"),
    path('viewAdminFeedbackUser/<int:id>',userviews.viewAdminFeedbackUser,name="viewAdminFeedbackUser"),
    path('viewBakerFeedbackUser/<int:id>',userviews.viewBakerFeedbackUser,name="viewBakerFeedbackUser"),
    path('logout/',site_adminviews.logout,name="logout"),
    path('viewFeedbackAdmin/<int:id>',site_adminviews.viewFeedbackAdmin,name="viewFeedbackAdmin"),
    path('viewFeedbackBaker/<int:id>',homebakerviews.viewFeedbackBaker,name="viewFeedbackBaker"),
    path('userPaymentAction/',userviews.userPaymentAction,name="userPaymentAction"),
    path('viewBakerOrderByAdmin/',site_adminviews.viewBakerOrderByAdmin,name="viewBakerOrderByAdmin"),
    path('viewBakersOrder/',site_adminviews.viewBakersOrder,name="viewBakersOrder"),
    path('bakerOrderDetailsActionAdmin/<int:id>/<int:bid>',site_adminviews.bakerOrderDetailsActionAdmin,name="bakerOrderDetailsActionAdmin"),
    path('adminPayment/<int:price>/<int:bid>/<int:oid>',site_adminviews.adminPayment,name="adminPayment"),
    path('adminPaymentAction',site_adminviews.adminPaymentAction,name="adminPaymentAction"),
    path('cancelorder/<int:id>',userviews.cancelorder,name="cancelorder"),
    path('refundPayment/<int:price>/<int:uid>/<int:oid>',site_adminviews.refundPayment,name="refundPayment"),
    path('refundPaymentAction',site_adminviews.refundPaymentAction,name="refundPaymentAction"),
    # path('markdelivered/<int:id>',site_adminviews.markdelivered,name="markdelivered"),
    # path('markdeliveredbaker/<int:id>',homebakerviews.markdeliveredbaker,name="markdeliveredbaker"),
    path('markdeliveredstaff/<int:id>',staffviews.markdeliveredstaff,name="markdeliveredstaff"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
