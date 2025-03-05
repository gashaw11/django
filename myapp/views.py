from django.shortcuts import render
from .models import Product

def hello_world(request):
    products = Product.objects.all()
    return render(request, 'hello.html',{'products':products})

