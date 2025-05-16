from django import template

register=template.Library()

@register.simple_tag(name="status")
def status(order_status):
    status=["CONFIRMED","PROCCESSED","DELIVERED","REJECTED"]
    return status[order_status-1]