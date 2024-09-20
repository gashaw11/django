
from django.urls import path
from . import views
urlpatterns = [
    #news/articles/2024/ this is passed to the year_archive function.
path("articles/<int:year>/", views.year_archive),
path("articles/<int:year>/<int:month>/", views.month_archive),
path("articles/<int:year>/<int:month>/<int:pk>/", views.article_detail),
 ]