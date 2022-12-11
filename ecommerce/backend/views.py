from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from .models import Vendoradd
import os
# Create your views here.

#for admin index
def indexpage(request):
    return render(request,'index.html')
#for add product
def new_product(request):
    return render(request,'add-new-product.html')

#for all products

def all_products(request):
    return render(request,'products.html')

#for orders

def order_list(request):
    return render(request,'order-list.html')

def order_details(request):
    return render(request,'order-detail.html')


#invoices
def invoice(request):
    return render(request,'invoice.html')
 #reports

def reports(request):
    return render(request,'reports.html')

def admin(request):
    return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        username= request.post['username']
        password= request.post['password']
    user=authenticate(request,user=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('index.html')


# def register(request):
#     if request.method == 'POST':
#         form= UserCreationForm(request.POST)
    
#         data={
#         'name':request.post['name'],
#         'email':request.post['email'],
#         'contact':request.post['contact'],
#         'gst':request.post['gst'],
#         'password':request.post['pass']
#         }
#         if data.is_valid():
#             user= data.save()
#             context={'form':form }
#             return redirect(request,'login.html',context)

# def register(request):
#     if request.method == 'POST':
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#         context={'form':form}
#     else:
#      return render(request,'sign-up.html',context)

def register(request):
    if request.method == 'POST':
        name=request.POST['name']  
        email=request.POST['email'] 
        conatct=request.POST['contact'] 
        gst=request.POST['gst'] 
        password=request.POST['pass']
        cpass=request.POST['cpass']
        image=request.FILES['image']
        if password==cpass:
            if User.objects.filter(vendorname=name).exists():
                return HttpResponse("<script>alert('password doesnot mached')</script>")
            elif User.objects.filter(email=email).exists():
                return HttpResponse("<script>alert('Email Exists')</script>")                
            else:
                user=User.objects.create_user(vendorname=name,vendoremail=email,vednorcontactno=conatct,vendorgistn=gst,password=password,vendorimage=image)
                document=Vendoradd.objects.create(file=image)
                user.save()
                document.save()
        else:
            return HttpResponse("<script>alert('password doesnot mached')</script>")
        return redirect('administrator/')   

    # else:
    return render(request,'sign-up.html')

