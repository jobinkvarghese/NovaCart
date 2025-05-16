from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cart/',views.cart,name='cart'),
    path('add_to_cart/',views.add_to_cart,name="add_to_cart"),
    path('remove_cart_item/<int:pk>',views.remove_cart_item,name="remove_cart_item"),
    path('checkout/',views.checkout,name="checkout"),
    path('orders/',views.orders,name="orders")
]