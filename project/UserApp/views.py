from django.shortcuts import render,redirect
from .models import *
from random import randint

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def login(request):
    return render(request, 'login.html')

def registerpage(request):
    return render(request, 'register.html')


def carpenter(request):
    return render(request, 'carpenter.html')
def cleaning(request):
    return render(request, 'cleaning.html')
def electrician(request):
    return render(request, 'electrician.html')
def mason(request):
    return render(request, 'mason.html')
def painter(request):
    return render(request, 'painter.html')
def plumber(request):
    return render(request, 'plumber.html')
def schedule(request):
    return render(request, 'schedule.html')




def RegisterUser(request):
    if request.POST['role']=='Customer':
        role = request.POST['role']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']


        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already Exist"
            return render(request, "register.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcustomer = Customer.objects.create(user_id=newuser,name=name,phone=phone)
                return render(request,"otpverify.html",{'email':email}) 
            else:
                message = "password does not match"
                return render(request, 'register.html',{'msg':message})
    
    else:
        if request.POST['role']=='Service_Provider':
            role = request.POST['role']
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            password = request.POST['password']
            cpassword = request.POST['cpassword']


            user = UserMaster.objects.filter(email=email)

            if user:
                message = 'User already Exist'
                return render(request, "register.html",{'msg':message})
            else:
                if password == cpassword:
                    otp = randint(100000,999999)
                    newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                    newserviceprovider = ServiceProvider.objects.create(user_id=newuser,name=name,phone=phone)
                    return render(request,"otpverify.html",{'email':email})
                else:
                    message = "password does not match"
                    return render(request, 'register.html',{'msg':message})


def OTPpage(request):
    return render(request,"otpverify.html")

def OtpVerify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])
    
    user = UserMaster.objects.get(email=email)
    
    if user:
        if user.otp == otp:
            message = "otp verify successfully"
            return render(request, 'login.html',{'msg':message})
        else:
            message = "otp is incorrect"
            return render(request, 'otpverify.html',{'msg':message})
    else:
        return render(request, 'register.html')


def LoginUser(request):
    if request.POST['role']=="Customer":
        email = request.POST['email']
        password = request.POST['password']

        user = UserMaster.objects.get(email=email)

        if user:
            if user.password == password and user.role=="Customer":
                cust = Customer.objects.get(user_id=user)
                request.session['id']=user.id
                request.session['role']=user.role
                request.session['name']=cust.name
                request.session['email']=user.email
                request.session['phone']=cust.phone
                return redirect('index')
            else:
                message = "password does not match"
                return render(request, 'login.html',{'msg':message})
        else:
            message = "User does not exist"
            return render(request, 'login.html',{'msg':message})

    elif request.POST['role']=="Service_Provider":
        email = request.POST['email']
        password = request.POST['password']

        user = UserMaster.objects.get(email=email)

        if user:
            if user.password == password and user.role=="service_provider":
                servicepro = ServiceProvider.objects.get(user_id=user)
                request.session['id']=user.id
                request.session['role']=user.role
                request.session['name']=servicepro.name
                request.session['email']=user.email
                request.session['phone']=servicepro.phone
                return redirect('index')
            else:
                message = "password does not match"
                return render(request, 'login.html',{'msg':message})
        else:
            message = "User does not exist"
            return render(request, 'login.html',{'msg':message})



def Profile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    cust = Customer.objects.get(user_id=user)
    return render(request, 'profile.html',{'user':user,'cust':cust})

def UpdateProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Customer":
        cust = Customer.objects.get(user_id=user)
        cust.address = request.POST['address']
        cust.city = request.POST['city']
        cust.state = request.POST['state']
        cust.pincode = request.POST['pincode']
        cust.save()
        url = f'/profile/{pk}'
        return redirect(url)









