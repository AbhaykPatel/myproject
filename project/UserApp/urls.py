from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    
    path("login/",views.login,name="login"),
    path("registerpage/",views.registerpage,name="registerpage"),
    path("register/",views.RegisterUser,name="register"),

    
    path("carpenter/",views.carpenter,name="carpenter"),
    path("cleaning/",views.cleaning,name="cleaning"),
    path("electrician/",views.electrician,name="electrician"),
    path("mason/",views.mason,name="mason"),
    path("painter/",views.painter,name="painter"),
    path("plumber/",views.plumber,name="plumber"),
    path("schedule/",views.schedule,name="schedule"),

    path("otppage/",views.OTPpage,name="otppage"),
    path('otpverify/',views.OtpVerify,name="otpverify"),

    path("loginuser/",views.LoginUser,name="loginuser"),

    path("profile/<int:pk>",views.Profile,name="profile"),
    path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),



]
