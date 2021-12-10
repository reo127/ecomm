from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catagory/<str:cataNmae>', views.catagory, name="catagory"),
    path('product/<int:sno>', views.product, name="product"),
    path('cartHandle/', views.cartHandle, name="cartHandle"),
    path('cart/', views.cart, name="cart"),
    path('belling/<int:sno>', views.belling, name="belling"),
    path('search/', views.search, name="search"),
    path('login', views.login, name="login"),
    path('singup', views.singup, name="singup"),
    path('singout', views.singout, name="singout"),
    path('delectCart/<int:sno>', views.delectCart, name="delectCart"),
    path('orderHandle/<int:sno>', views.orderHandle, name="orderHandle"),
]

