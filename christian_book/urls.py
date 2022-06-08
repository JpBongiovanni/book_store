from django.contrib import admin
from django.urls import path, include

#the Admin path is not utilized, but I did include it for future development
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product_app.urls')),
]
