from django.urls import path
from .views import get_info, get_products_about, detail, add_products, update_products


app_name = 'products'
urlpatterns = [
    path('', get_info, name="get_info"),
    path('products/<int:pk>', get_products_about, name="get_products_about"),
    path('products/detail/<int:pk>', detail, name="detail"),
    path('add_products', add_products, name="add_products"),
    path('update/<int:pk>', update_products, name="update"),
]



