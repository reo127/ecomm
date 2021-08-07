from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    AllProds = Product.objects.all()
    cata = Product.objects.values('category', 'id')
    cats = {item['category'] for item in cata}
    params = {"AllProd": AllProds, 'cats': cats}
    return render(request, 'core/index.html', params)


def catagory(request, cataNmae):
    AllProds = Product.objects.filter(category=cataNmae)
    params = {"AllProd": AllProds}
    return render(request, 'core/catagory.html', params)


def product(request, sno):
    product = Product.objects.filter(id=sno)
    params = {'product': product}
    return render(request, 'core/product.html', params)


def belling(request):
    return render(request, 'core/belling.html')


def search(request):
    return render(request, 'core/search.html')


def login(request):
    return HttpResponse('This apps get')


def singup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        addres = request.POST['addres']
        phone = request.POST['phone']
        password = request.POST['password']
        # confromPassword = request.POST['confromPassword']

        user = User.objects.create_user(username, email, password)
        user.home_addres = addres
        user.phone_number = phone
        user.save()
    else:
        return HttpResponse('This app acpets POST but htis methid is get')

    return redirect('/')
