from django.urls import path
from . import views


urlpatterns = [
   path('',views.indexpage,name='index'),
   path('blog/',views.blog,name='blog'),
   path('contact-us/',views.contact,name='contact'),
   path('about-us/',views.about,name='about'),
]