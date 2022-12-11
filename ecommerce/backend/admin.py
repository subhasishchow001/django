from django.contrib import admin
from .models import Vendoradd
# Register your models here.

class Vendors(admin.ModelAdmin):
    list_display=('vendorname','vendoraddress','vednorcontactno','vendoremail','vendorimage','vendorgistn')
    
admin.site.register(Vendoradd,Vendors)