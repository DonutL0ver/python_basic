from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.urls import reverse
from django.shortcuts import render
from .models import Product
"""
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
"""
def ProductListView(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})

def ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    return render(DetailView, 'myapp/product_detail.html',{'model': model} )

def index_view(request):
    return render(request, 'myapp/index.html')
def home_view(request):
    return render(request, 'myapp/home.html')

def my_view(request):
    context = {'my_model_list': Product.objects.all()}
    return render(request, 'myapp/my_template.html', context)



