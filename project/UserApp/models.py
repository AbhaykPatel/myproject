from django.db import models

# Create your models here.
class UserMaster(models.Model):
    
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)
    class Meta():
        db_table = 'usermaster'

class Customer(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    class Meta():
        db_table = 'customer'

class ServiceProvider(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    service_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    profile_pic = models.ImageField(upload_to='static/img/serviceprovider')
    class Meta():
        db_table = 'serviceprovider'
    
class Service(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    service_name = models.CharField(max_length=50)
    service_date = models.DateField()
    service_time = models.TimeField()
    class Meta():
        db_table = 'service'