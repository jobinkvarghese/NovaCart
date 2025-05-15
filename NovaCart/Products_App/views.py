from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    featured_product=Product.objects.order_by('priority')[0:4]
    latest_product=Product.objects.order_by('-created_at')[:4]
    context={
       'featured_product':featured_product,
       'latest_product':latest_product
    }

    return render(request,'website/index.html',context=context)

def product(request):
    page_value=1
    if request.GET:
     page_value=request.GET.get('page')
    product_list=Product.objects.order_by('priority')
    paginator_obj=Paginator(product_list,2)
    product_page=paginator_obj.get_page(page_value)
    context={
        'items':product_page
            }
    return render(request,'website/product.html',context)

def product_details(request,pk):
    instance=Product.objects.get(pk=pk)
    context={
       'record':instance
    }
    return render(request,'website/product_details.html',context=context)