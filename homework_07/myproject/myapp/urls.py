from django.urls import path
from .views import ProductListView, ProductDetailView, home_view

urlpatterns = [
    path('', home_view, name='myapp_home'),
    path('home/', home_view, name='home_view'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

