from django.contrib import admin
from django.urls import path
from .views import get_products
from django.urls import path

urlpatterns = [
    path('products/', get_products),
]
