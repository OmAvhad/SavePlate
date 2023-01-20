from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Donations,UserDetials
from django.contrib import messages 
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.
@csrf_exempt
def dashboard(request,template_name="user/dashboard.html"):
    return render(request,template_name)