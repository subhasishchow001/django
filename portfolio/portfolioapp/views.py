from django.views.generic import ListView   
from .models import *
from django.shortcuts import render
from django.views.generic.detail import DetailView

# Create your views here.

def indexpage(request):
    return render(request,'index.html')

# class Blogdetailview(ListView):
#      blogdetail=Blogposts.objects.all()
#      template_name="page.html"

def blog(request):
    blogs=Blogposts.objects.all()
    context={
        'blogs': blogs
    }
    return render(request,'blog.html',context)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

