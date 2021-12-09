from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Product, Orders, Cart
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages


def home(request):
    AllProds = Product.objects.all()
    cata = Product.objects.values('category', 'id')
    cats = {item['category'] for item in cata}
    print(cats)
    if request.user.is_authenticated:
        cartLenth = Cart.objects.filter(belongsTo = request.user).count()
    else:
        cartLenth = 0

    params = {"AllProd": AllProds, 'cats': cats, "cartLenth": cartLenth}
    return render(request, 'core/index.html', params)


def cartHandle(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            originalId = request.POST['prodId']
            product_name = request.POST['prodName']
            price = request.POST['prodPrice']
            Cart.objects.create(originalId=originalId, product_name=product_name, price=price, belongsTo=request.user)
            messages.success(request, f"{product_name} is added to your cart")
            return HttpResponseRedirect('/')

def cart(request):
    if request.user.is_authenticated:
        cartProd = Cart.objects.filter(belongsTo = request.user)
        params = {"prod": cartProd}
        return render(request, "core/cart.html", params)
    else:
        return render(request, "core/cart.html")


def catagory(request, cataNmae):
    AllProds = Product.objects.filter(category=cataNmae)
    params = {"AllProd": AllProds}
    return render(request, 'core/catagory.html', params)


def product(request, sno):
    product = Product.objects.filter(id=sno)
    params = {'product': product}
    return render(request, 'core/product.html', params)


def belling(request, sno):
    prod = Product.objects.filter(id=sno)
    for prod in prod:
        pass
    params = {'prod': prod}
    return render(request, 'core/belling.html', params)


def search(request):
    sq = request.GET.get('quary')
    allProd = Product.objects.filter(product_name__icontains=sq)
    params = {'allProd': allProd}
    return render(request, 'core/search.html', params)


def orderHandle(request, sno):
    if request.method == "POST":
        product_sno = sno
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        landMark = request.POST['landMark']
        opitonlAddress = request.POST['address2']
        state = request.POST['state']
        zip = request.POST['zip']
        payment = request.POST['payment']

        Orders.objects.create(product_sno=product_sno, phone=phone, email=email, address=address, landMark=landMark, opitonlAddress=opitonlAddress, state=state, zip=zip, payment=payment)
    messages.success(request, "your Order placed successfully, Thanks to order with us")

    return redirect('/')

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
