from django.db import models
from django.contrib.auth.models import User

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
    type = models.CharField(max_length=20,choices=USER_TYPE,blank=True, null=True)
    
    class Meta:
        db_table = "USER_DETAILS"