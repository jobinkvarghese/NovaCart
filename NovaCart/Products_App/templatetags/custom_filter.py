from django import template

register=template.Library()

@register.filter(name='chunk') #custom_filter
def chunks(list,chunk_size):
    chunk=[]
    i=0
    for item in list:
        chunk.append(item)
        i+=1
        if(i==chunk_size):
            yield chunk
            chunk=[]
            i=0
    if chunk:
     yield chunk

@register.simple_tag #custom_tag
def multiply(a,b):
    return a*b

