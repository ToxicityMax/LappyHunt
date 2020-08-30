from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name="HOME"),
    path("laptop/", views.laptop, name="LAPTOP"),
    path("cart/", views.cart, name="CART"),
    #path("sort/", views.sort, name="SORT"),
    #path('laptop/details/<slug:slug>', detail),
]
