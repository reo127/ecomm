from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='productttttttttttt'),
    path('cetagory/', views.cetagory, name='crtagory'),
    path('belling/', views.belling, name='belling'),
    path('search/', views.search, name='search'),
]
