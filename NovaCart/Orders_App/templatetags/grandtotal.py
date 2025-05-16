from django import template

register=template.Library()

@register.simple_tag(name="grand")
def grand(obj):
    total=0
    for data in obj.added_items.all():
        total=total+data.quantity*data.product.price
    return total