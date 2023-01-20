from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Donations,UserDetials
from django.contrib import messages 
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@login_required
def dashboard(request,template_name="ngo/dashboard.html"):
    donation_list = Donations.objects.filter(to_user__id=request.user.id,received_status=False)
    food_bank_list = Donations.objects.filter(to_user__id=request.user.id,received_status=True)
    user_details = UserDetials.objects.get(user__id=request.user.id)
    if request.method == "POST":
        postdata = request.POST
        
        if postdata['donation_received'] == 1:
            donation_id = postdata['donation_id']
            try:
                Donations.objects.filter(id=donation_id).update(received_status=True,received_at=datetime.now())
                messages.success(request,'Order received.')
            except Exception as e:
                print(e)
                messages.error(request,'Something went wrong.')
                
        elif postdata['food_bank_donated'] == 1:
            address = postdata['address']
            try:
                Donations.objects.filter(to_user__id=request.user.id,received_status=True,donated_status=False).update(donated_status=True,donated_at=datetime.now(),donated_at_location=address)
                messages.success(request,'All Donated.')
            except:
                print(e)
                messages.error(request,'Something went wrong.')
    return render(request,template_name,{'user_details',user_details})