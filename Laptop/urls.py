from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name="HOME"),
    path("laptop", views.laptop, name="LAPTOP"),
]
