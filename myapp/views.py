from django.shortcuts import render,redirect
from .models import Product

def hello_world(request):
    # Fetch products from the database
    

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
        
        "menu": menu,  # Taqueria menu
        "total_price": total_price,  # Total price of selected menu items
        "selected_items": selected_items  # Selected menu items
    })


def coke_machine(request):
    # Initialize session variables if not set
    if "amount_due" not in request.session:
        request.session["amount_due"] = 50
        request.session["inserted_coins"] = []
        request.session["total_inserted"] = 0
        request.session["change_owed"] = 0

    error_message = ""

    if request.method == "POST":
        try:
            coin = int(request.POST.get("coin", 0))  # Get coin input
            if coin in [5, 10, 25]:  # Valid coins only
                request.session["inserted_coins"].append(coin)
                request.session["total_inserted"] += coin
                request.session["amount_due"] = max(0, 50 - request.session["total_inserted"])
                request.session["change_owed"] = max(0, request.session["total_inserted"] - 50)
                request.session.modified = True  # Save session changes
            else:
                error_message = "Invalid coin. Please insert 5, 10, or 25 cents."
        except ValueError:
            error_message = "Invalid input. Please enter a number."

    return render(request, "myapp/home.html", {
        "amount_due": request.session["amount_due"],
        "inserted_coins": request.session["inserted_coins"],
        "total_inserted": request.session["total_inserted"],
        "change_owed": request.session["change_owed"],
        "error_message": error_message,
    })

def reset_coke(request):
    request.session.flush()  # Clear session data
    return redirect("coke_machine")