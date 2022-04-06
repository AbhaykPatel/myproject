from django.shortcuts import render,redirect
from .models import *
from random import randint

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def about2(request):
    return render(request, 'about2.html')

def contact(request):
    return render(request, 'contact.html')
def contact2(request):
    return render(request, 'contact2.html')

def login(request):
    return render(request, 'login.html')

def registerpage(request):
    return render(request, 'register.html')

def customerindex(request):
    return render(request, 'customerindex.html')



def carpenter(request):
    return render(request, 'service/carpenter.html')
def cleaning(request):
    return render(request, 'service/cleaning.html')
def electrician(request):
    return render(request, 'service/electrician.html')
def mason(request):
    return render(request, 'service/mason.html')
def painter(request):
    return render(request, 'service/painter.html')
def plumber(request):
    return render(request, 'service/plumber.html')

def carpenter2(request):
    return render(request, 'service_afterlogin/carpenter2.html')
def cleaning2(request):
    return render(request, 'service_afterlogin/cleaning2.html')
def electrician2(request):
    return render(request, 'service_afterlogin/electrician2.html')
def mason2(request):
    return render(request, 'service_afterlogin/mason2.html')
def painter2(request):
    return render(request, 'service_afterlogin/painter2.html')
def plumber2(request):
    return render(request, 'service_afterlogin/plumber2.html')





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
                return redirect('customerindex')
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
                return redirect('customerindex')
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

def schedule(request,pk):
    user = UserMaster.objects.get(pk=pk)
    cust = Customer.objects.get(user_id=user)
    return render(request, 'schedule.html',{'user':user,'cust':cust})

def ServicePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Customer":
        cust = Customer.objects.get(user_id=user)
        cust.name = request.POST['name']
        cust.phone = request.POST['phone']
        cust.address = request.POST['address']
        cust.city = request.POST['city']
        cust.state = request.POST['state']
        cust.pincode = request.POST['pincode']
        cust.save()
        url = f'/schedule/{pk}'
        return redirect(url)


def ServiceSubmit(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Customer":
        service = Service.objects.get(user_id=user)
        service.service_name = request.POST['service_name']
        service.service_date=request.POST['date']
        service.service_time=request.POST['time']
        service.save()
    
        newservice = Service.objects.create(user_id=user,service_name=service_name,service_date=service_date,service_time=service_time)
        
        message = "Service Added Successfully"
        
        return render(request, 'schedule.html',{'msg':message})

def ServiceList(request,pk):  
    all_service = Service.objects.all()
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Customer":
        cust = Customer.objects.get(user_id=user)
        return render(request, 'service_list.html',{'allservice':all_service,'user':user,'cust':cust})


















 











