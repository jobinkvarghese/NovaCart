from django.db import models
from Customers_App.models import Customer
from Products_App.models import Product

# Create your models here.

class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=(
        (LIVE,'live'),
        (DELETE,'delete')
    )
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    OREDER_REJECTED=4
    STATUS_CHOICES=(
        (ORDER_PROCESSED,'Order Processed'),
        (ORDER_DELIVERED,'Order Delivered'),
        (OREDER_REJECTED,'Order Rejected')
    )

    owner=models.ForeignKey(Customer,related_name="orders",on_delete=models.SET_NULL,null=True)
    grand_total=models.FloatField(default=0.0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    order_status=models.IntegerField(choices=STATUS_CHOICES,default=CART_STAGE)

    def __str__(self):
        return self.owner.name

   
class OrderedItem(models.Model):
    product=models.ForeignKey(Product,related_name="added_products",on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    size=models.CharField(max_length=100,default="undefined")
    owner=models.ForeignKey(Order,related_name="added_items",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)