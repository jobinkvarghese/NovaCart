from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    return render(request,'website/index.html')

def product(request):
    product_list=Product.objects.all()
    context={
        'items':product_list
            }
    return render(request,'website/product.html',context)

def product_details(request):
    return render(request,'website/product_details.html')