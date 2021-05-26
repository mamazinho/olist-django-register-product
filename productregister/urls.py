from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home),
    path('products/', views.list_products, name='products'),
    path('products/<id>', views.alter_products, name='products-form'),
    path('product/new', views.create_product, name='products-new'),
    path('categories/', views.list_categories, name='categories'),
    path('categories/<id>', views.alter_categories, name='categories-form'),
    path('category/new', views.create_category, name='categories-new'),
]