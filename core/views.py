from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def cetagory(request):
    # return render(request, 'core/cetagory.html')
    return HttpResponse("working")

def product(request):
    return render(request, 'core/product.html')

def belling(request):
    return render(request, 'core/belling.html')

def search(request):
    return render(request, 'core/search.html')
    
    