from django.shortcuts import render
from .models import Product

# Create your views here.


def home(request):
    AllProds = Product.objects.all()
    cata = Product.objects.values('category', 'id')
    cats = {item['category'] for item in cata}
    print(cats)
    params = {"AllProd": AllProds, 'cats':cats}
    return render(request, 'core/index.html', params)


def catagory(request, cataNmae):
    AllProds = Product.objects.get(category=cataNmae)
    params = {"AllProd": AllProds}
    return render(request, 'core/catagory.html', params)


def product(request):
    return render(request, 'core/product.html')


def belling(request):
    return render(request, 'core/belling.html')


def search(request):
    return render(request, 'core/search.html')
