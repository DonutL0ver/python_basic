from django.urls import path, include
from . import views
from .views import ProductListView, ProductDetailView, home_view, index_view
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home_view, name='home'),
    path('index/', views.index_view, name='index'),
    path('product_list/', ProductListView, name='product_list'),
    path('product_detail/', ProductDetailView, name='product_detail'),
]


