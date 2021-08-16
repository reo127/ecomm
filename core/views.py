from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
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
    sq = request.GET.get('quary')
    allProd = Product.objects.filter(product_name=sq)
    params = {'allProd': allProd}
    return render(request, 'core/search.html', params)


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        loginUser = authenticate(username=email, password= password)
        if loginUser is not None:
            auth_login(request, loginUser)
            messages.success(request, "Your Login Sussfuly")
            return redirect('/')
    return HttpResponse('Thear is something worng chack the login view')


def singup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        addres = request.POST['addres']
        phone = request.POST['phone']
        password = request.POST['password']
        confromPassword = request.POST['confromPassword']

        if password == confromPassword:
            user = User.objects.create_user(username, email, password)
            user.home_addres = addres
            user.phone_number = phone
            user.save()
            messages.success(request, "Your Singup Succfull now place Login")
        else:
            return redirect('/') # Show django massage theare
    else:
        return HttpResponse('This app acpets POST but htis methid is get')

    return redirect('/')


def singout(request):
    logout(request)
    messages.error(request, "Logout Succful")
    return redirect('/')
