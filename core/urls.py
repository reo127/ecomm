from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catagory/', views.catagory, name="catagory"),
    path('product/', views.product, name="product"),
    path('belling/', views.belling, name="belling"),
    path('search/', views.search, name="search"),
]
