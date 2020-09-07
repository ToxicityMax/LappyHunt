from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Laptop.urls"),),
    path("faq", include("faq.urls"),),
    path("faq", include("cart.urls"),),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
