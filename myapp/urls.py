from django.urls import path
from .views import hello_world,coke_machine,reset_coke

urlpatterns = [
    path('',    taqueria_menu),
    path("coke/", coke_machine, name="coke_machine"),
    path("reset_coke/", reset_coke, name="reset_coke"),
]
