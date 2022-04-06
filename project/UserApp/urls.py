from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("about2/",views.about2,name="about2"),

    path("contact/",views.contact,name="contact"),
    path("contact2/",views.contact2,name="contact2"),


    path("customerindex/",views.customerindex,name="customerindex"),   
    path("login/",views.login,name="login"),
    
    path("registerpage/",views.registerpage,name="registerpage"),
    path("register/",views.RegisterUser,name="register"),

    
    path("carpenter/",views.carpenter,name="carpenter"),
    path("cleaning/",views.cleaning,name="cleaning"),
    path("electrician/",views.electrician,name="electrician"),
    path("mason/",views.mason,name="mason"),
    path("painter/",views.painter,name="painter"),
    path("plumber/",views.plumber,name="plumber"),

    path("carpenter2/",views.carpenter2,name="carpenter2"),
    path("cleaning2/",views.cleaning2,name="cleaning2"),
    path("electrician2/",views.electrician2,name="electrician2"),
    path("mason2/",views.mason2,name="mason2"),
    path("painter2/",views.painter2,name="painter2"),
    path("plumber2/",views.plumber2,name="plumber2"),


    path("otppage/",views.OTPpage,name="otppage"),
    path('otpverify/',views.OtpVerify,name="otpverify"),

    path("loginuser/",views.LoginUser,name="loginuser"),

    path("profile/<int:pk>",views.Profile,name="profile"),
    path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),

    path("schedule/<int:pk>",views.schedule,name="schedule"),
    path("servicepage/<int:pk>",views.ServicePage,name="servicepage"),
    path("servicesubmit/<int:pk>",views.ServiceSubmit,name="servicesubmit"),
    
    path("servicelist/<int:pk>",views.ServiceList,name="servicelist"),


]




