from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admindashboard/',views.indexpage,name='admin'),
    path('add-product/',views.new_product,name='add_product'),
    path('all-products/',views.all_products,name='all_products'),
    path('order-list/',views.order_list,name='order_list'),
    path('order-details/',views.order_list,name='order_details'),
    path('invoice/',views.invoice,name='invoice'),
    path('reports/',views.reports,name='reports'),
    #authentiations
    path("signup/",views.register, name="signup"),
    path('administrator/',views.admin,name='adminlogin'),
]
