from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Vendoradd

class Orderform(ModelForm):
    class Meta:
       model=Vendoradd
       fields=['vendorname','vendoraddress','vednorcontactno','vendoremail','vendorimage','vendorgistn']
