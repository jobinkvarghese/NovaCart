from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Customer
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.shortcuts import redirect

# Create your views here.
def user_account(request):
    context={}
    if request.method=="POST" and 'register' in request.POST :
        context['register']=True
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            user=User.objects.create_user(username=username,email=email,password=password)
            customer=Customer.objects.create(phone=phone,address=address,user=user,name=user.username)
            messages.success(request,"Registration Success")
            # return HttpResponseRedirect(reverse('home'))
        except Exception as p:
                error_msg="username already exists"
                messages.error(request,error_msg)

    if request.POST and 'login' in request.POST:
     context['register']=False
     username=request.POST.get('username')
     password=request.POST.get('password')
     user_auth=authenticate(request,username=username,password=password)
     if user_auth:
         if user_auth.is_active:
             login(request,user_auth)
             messages.success(request,"Login Success")
         else:
             messages.error(request,"User is Inactive")
     else:
        messages.error(request,"Invalid login credentials")
                
                    
    # print(request.user)
    return render(request,'website/user_account.html',context=context)


def logout(request):
    auth_logout(request)
    return redirect('home')