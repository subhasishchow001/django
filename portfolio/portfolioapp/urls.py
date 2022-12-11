from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
   path('',views.indexpage,name='index'),
   path('blog/',views.blog,name='blog'),
   path("blog/<int:id>/", views.blog_detail, name="blog_detail"),
   path('contact-us/',views.contact,name='contact'),
   path('about-us/',views.about,name='about'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)