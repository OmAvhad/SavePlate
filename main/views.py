from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password,check_password
from .models import UserDetials
from django.contrib import messages 

# Create your views here.
def home(request,template_name="main/index.html"):
    return render(request,template_name)

@csrf_exempt
def login_template(request,template_name="main/login.html"):
    if request.method == "POST":
        try:
            postdata = request.POST
            username = postdata['username']
            password = postdata['password']
            try:
                user = authenticate(username=username, password=password)
            except:
                user = None
            if user is not None:
                login(request,user)
                user_details_obj = UserDetials.objects.get(user__id=user.id)
                messages.success(request, "Logged In" )
                if user_details_obj.type == '2':
                    return redirect('org:dashboard')
                elif user_details_obj.type == '3':
                    return redirect('ngo:dashboard')
                elif user_details_obj.type == '4':
                    return redirect('user:dashboard')
            else:
                messages.error(request, "User not found")
        except Exception as e:
            messages.error(request, "Some Error Occured")

    return render(request,template_name)


@csrf_exempt
def register_template(request,slug,template_name="main/register.html"):
    type= slug
    if request.method == "POST":
        postdata = request.POST
        try:
            username = postdata['username']
            password = make_password(postdata['password'])
            first_name = postdata['name']
            email = postdata['email']
            type = postdata['type']
            try:
                user = User.objects.get(Q(username=username) | Q(email=email))
            except:
                user = None
            if user ==  None:
                user = User.objects.create(username=username,password=password,email=email,first_name=first_name)
                UserDetials.objects.create(user=user,type=type)
                login(request,user)
                messages.success(request, "Registered Successfully" )
                return redirect(register2_template,user_id=user.id)
            else:
                messages.error(request, "Username or Email already Exists.")
        except Exception as e:
            messages.error(request, "Some Error Occured")
    return render(request,template_name,{'type': type})


@csrf_exempt
def register2_template(request,user_id,template_name="main/register2.html"):
    user_id = user_id
    if request.method == "POST":
        postdata = request.POST
        try:
            id = postdata['id']
            address = postdata['address']
            state = postdata['state']
            city = postdata['city']
            pincode = postdata['pincode']
            try:
                user_details_obj = UserDetials.objects.filter(user__id=id).update(address=address,state=state,city=city,pincode=pincode)
            except:
                user_details_obj = None
            if user_details_obj:
                messages.success(request, "Address details updated Successfully.")
                if user_details_obj.type == '2':
                    return redirect('org:dashboard')
                elif user_details_obj.type == '3':
                    return redirect('ngo:dashboard')
                elif user_details_obj.type == '4':
                    return redirect('user:dashboard')
            else:
                messages.error(request, "User not found.")
        except Exception as e:
            messages.error(request, "Some Error Occured.")
    return render(request,template_name,{'user_id': user_id})
    

def logout_url(request):
    logout(request)
    redirect('main:index')