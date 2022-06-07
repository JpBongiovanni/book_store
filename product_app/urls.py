from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('single_item/<str:item_id>', views.single_item, name="single_item"),
    path('search', views.search, name="search"),
    path('searchId', views.searchId, name="searchId"),
    path('upload_products', views.upload_products, name="upload_products"),
    path('add_more_product', views.add_more_product, name="add_more_product"),
    path('single_item/delete/<str:item_id>', views.delete, name="delete")
]