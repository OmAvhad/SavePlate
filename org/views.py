from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Donations,UserDetials
from django.contrib import messages 
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.
@login_required
def dashboard(request,template_name="org/dashboard.html"):
    applied_for_donation_list = Donations.objects.filter(from_user__id=request.user.id)
    user_details = UserDetials.objects.get(user__id=request.user.id)
    return render(request,template_name)