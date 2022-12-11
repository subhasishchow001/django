from django.views.generic import ListView   
from .models import *
from django.shortcuts import render

# Create your views here.

def indexpage(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

