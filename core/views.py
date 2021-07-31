from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    AllProds = Product.objects.all()
    params = {"AllProd": AllProds}
    return render(request, 'core/index.html', params )

def catagory(request):
    return render(request, 'core/catagory.html')

def  product(request):
    return render(request, 'core/product.html')

def belling(request):
    return render(request, 'core/belling.html')

def search(request):
    return render(request, 'core/search.html')