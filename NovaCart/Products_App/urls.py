from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product/',views.product,name='product'),
    path('product_details/<int:pk>',views.product_details,name='product_details'),
]
