from django.shortcuts import render
from .models import Product

def hello_world(request):
    # Fetch products from the database
    products = Product.objects.all()

    # Taqueria menu as a list of dictionaries (like products)
    menu = [
        {"name": "Baja Taco", "price": 4.25},
        {"name": "Burrito", "price": 7.50},
        {"name": "Bowl", "price": 8.50},
        {"name": "Nachos", "price": 11.00},
        {"name": "Quesadilla", "price": 8.50},
        {"name": "Super Burrito", "price": 8.50},
        {"name": "Super Quesadilla", "price": 9.50},
        {"name": "Taco", "price": 3.00},
        {"name": "Tortilla Salad", "price": 8.00},
    ]

    selected_items = []
    total_price = 0

    if request.method == "POST":
        selected_items = request.POST.getlist("items")  # Get selected items
        total_price = sum(item["price"] for item in menu if item["name"] in selected_items)

    return render(request, 'myapp/home.html', {
        "products": products,  # Products from the database
        "menu": menu,  # Taqueria menu
        "total_price": total_price,  # Total price of selected menu items
        "selected_items": selected_items  # Selected menu items
    })
