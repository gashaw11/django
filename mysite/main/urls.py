from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    # path("v1/", views.v1, name="view 1"),  # Uncomment or modify this line if needed
    path("create/", views.create, name="create"),
    path("", views.home, name="home"),
]