from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from Products_App.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='user_account')
def cart(request):
    try:
        user=request.user
        customer=user.customer
        order_obj,created=Order.objects.get_or_create(
                owner=customer,
                order_status=Order.CART_STAGE,
            )
        context={
            "cart":order_obj
        }
    except Exception:
        messages.error(request,"Please Login")
    return render(request,'website/cart.html',context)
@login_required(login_url='user_account')
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        size=request.POST.get('size')
        product_obj=Product.objects.get(pk=product_id)
        order_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE,
        )
        ordered_item,created=OrderedItem.objects.get_or_create(
            owner=order_obj,
            product=product_obj,
            size=size,
        )
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            ordered_item.quantity=ordered_item.quantity+quantity
            ordered_item.save()
    return redirect('cart')

def remove_cart_item(request,pk):
    instance=OrderedItem.objects.get(pk=pk)
    if instance:
     instance.delete()
    return redirect('cart')

def checkout(request):
    try:
        if request.POST:
            user=request.user
            customer=user.customer
            total=request.POST.get('grand_total')
            order_obj=Order.objects.create(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            order_obj.order_status=Order.ORDER_CONFIRMED
            order_obj.grand_total=total
            order_obj.save()
            if order_obj:
                status_message="ORDER PLACED SUCCESSFULLY"
                messages.success(request,status_message)
            else:
                status_message="CART IS EMPTY"
                messages.error(request,status_message)
    except Exception as e:
        status_message="CART IS EMPTY"
        messages.error(request,status_message)

    return redirect('cart')

@login_required(login_url='user_account')
def orders(request):
    user=request.user
    customer=user.customer
    orders_obj=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={
        'order':orders_obj
    }
    return render(request,'website/order.html',context=context)