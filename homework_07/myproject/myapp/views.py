from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
def index(request):
    return render(request, 'index.html')
def home_view(request):
    return render(request, 'home.html')


