from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    return render(request,'website/index.html')

def product(request):
    obj=Product.objects.all()
    return render(request,'website/product.html',{'data':obj})

def product_details(request):
    return render(request,'website/product_details.html')