from django.views.generic import ListView   
from .models import *
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponse

# Create your views here.

def indexpage(request):
    return render(request,'index.html')

def blog_detail(request,id):
    blog=Blogposts.objects.get(id=id)
    conns={
        "blog":blog
    }
    return render(request,'single-blog.html',conns)

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

