from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    return render(request,'website/index.html')

def product(request):
    page_value=1
    if request.GET:
     page_value=request.GET.get('page')
    product_list=Product.objects.all()
    paginator_obj=Paginator(product_list,2)
    product_page=paginator_obj.get_page(page_value)
    context={
        'items':product_page
            }
    return render(request,'website/product.html',context)

def product_details(request):
    return render(request,'website/product_details.html')