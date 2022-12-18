from django.urls import path
from backend.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admindashboard/',indexpage,name='admindash'),
    path('add-product/',new_product,name='add_product'),
    path('all-products/',all_products,name='all_products'),
    path('order-list/',order_list,name='order_list'),
    path('order-details/',order_list,name='order_details'),
    path('invoice/',invoice,name='invoice'),
    path('reports/',reports,name='reports'),
    #authentiations
    # path("signup/",views.register, name="signup"),
    path('administrator/',admin,name='adminlogin'),
]
