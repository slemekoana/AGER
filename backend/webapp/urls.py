#from ast import patterns #deprecated
from django import views
from django.urls import path
from . import views

# to add routes to the main url
urlpatterns = [path('', views.index, name= 'index'),
                path('signup', views.register, name='register'),
                path('login', views.login, name='login'),
                path('logout', views.logout, name='logout'),
                path('shop', views.shop, name='shop'),
                path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
                path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
                path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
                path('cart/cart-detail/',views.cart_detail, name='cart_detail')]
