#from ast import patterns #deprecated
from django import views
from django.urls import path
from . import views

# to add routes to the main url
urlpatterns = [path('', views.index, name= 'index'),
                path('signup', views.register, name='register'),
                path('login', views.login, name='login'),
                path('logout', views.logout, name='logout'),
                path('shop', views.shop, name='shop')]
