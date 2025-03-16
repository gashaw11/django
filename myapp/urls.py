from django.urls import path
from .views import product_item,coke_machine,reset_coke,home_view

urlpatterns = [
    path('', home_view,name="home_view"),
    path("product/", product_item,name="product_item"),
    path("coke/", coke_machine, name="coke_machine"),
    path("reset_coke/", reset_coke, name="reset_coke"),
]
