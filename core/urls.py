from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catagory/<str:cataNmae>', views.catagory, name="catagory"),
    path('product/<int:sno>', views.product, name="product"),
    path('belling/', views.belling, name="belling"),
    path('search/', views.search, name="search"),
]

