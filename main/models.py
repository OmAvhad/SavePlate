from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserDetials(models.Model):
    
    USER_TYPE =  (
        ("0","ADMIN"),
        ("1","FOOD RETAILER"),
        ("2","ORGANIZATION"),
        ("3","NGO"),
        ("4","USER")
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=400, blank=True,null=True)
    state = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=255,blank=True,null=True)
    pincode = models.IntegerField(blank=True,null=True)
    phone = models.BigIntegerField(blank=True,null=True)
    type = models.CharField(max_length=20,choices=USER_TYPE,blank=True, null=True)
    
    class Meta:
        db_table = "USER_DETAILS"
        
class Donations(models.Model):
    
    food_name = models.CharField(max_length=255,null=True,blank=True)
    plate_size = models.IntegerField(default=0,null=True,blank=True)
    reason = models.TextField(null=True,blank=True)
    from_user = models.ForeignKey(User, related_name="FromUser", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="ToUser", on_delete=models.CASCADE)
    applied_at = models.DateTimeField(blank=True, null=True)
    received_status = models.BooleanField(default=False)
    received_at = models.DateTimeField(blank=True, null=True)
    donated_status = models.BooleanField(default=False)
    donated_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = "DONATIONS"