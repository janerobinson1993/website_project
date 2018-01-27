from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('JanesKitchen_site/', include('JanesKitchen_site.urls')),
    path('admin/', admin.site.urls),
    ]
