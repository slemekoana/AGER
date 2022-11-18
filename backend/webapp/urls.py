#from ast import patterns #deprecated
from django import views
from django.urls import path
from . import views

# to add routes to the main url
urlpatterns = [path('', views.index, name= 'index')]
