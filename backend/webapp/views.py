from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect #possibly not needed
from django.template import loader #possibly not needed
from django.contrib.auth.models import auth 
from .models import Product, User, Cart, CartItem
from django.contrib.auth.decorators import login_required
# from cart.cart import Cart // not working
from rest_framework.authtoken.models import Token
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
import logging #only for test


# Create your views here.
def index(request):
  context = {}
  return render(request, 'index.html',{})

def register(request):
  #Registers a user in the User database from the admin panel
  if request.method == "POST":
    #username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    username = email.split('@')[0] # for a future implementation, check the format
    """ password2 = request.POST["password2"]
    if password == password2: """
      #we check if the email already exist in the User database
    if email and User.objects.filter(email = email ).exists():
        messages.info(request, "Email already used.")
        return redirect('/') 
        """ elif User.objects.filter(username = username ).exists():
        messages.info(request, "Username already used.")
        return redirect('') """
    else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.info(request, "User registered, please login.")
        return redirect('/')
    """ else:
      messages.info(request, "Passwords don't match.") """
  else: 
    return redirect('/')

def login(request):
  if request.method == "POST":
    email = request.POST["email"]
    username = email.split('@')[0]
    password = request.POST["password"]

    user = auth.authenticate(username=username, password = password)
    if user is not None:
      auth.login(request, user) #auth does all the work for authentification in the User database from admin
      
      return redirect('/')
    else:
      messages.info(request, "Wrong email or password")
      return redirect("/")
  else:
    return redirect('/')

def logout(request):
  auth.logout(request)
  return redirect('/')



def shop(request):
  return render(request,'shop.html')

#@login_required(login_url="login") # using API Keys instead
@api_view(['POST'])
def cart_add(request, id, amount):
    parsed_body = json.loads(request.body)
    user  = parsed_body['user']
    cart, _ = Cart.objects.get_or_create( user = user) # try this otherswise find user in the body
    items, total = cart.add(id, amount = amount)
    #product = Product.objects.get(id=id)
    #cart.add(product=product)
    return Response([items, total]) 


#@login_required(login_url="login")
@api_view(['DELETE'])
def item_clear(request, id):
    parsed_body = json.loads(request.body)
    user  = parsed_body['user']
    cart, _ = Cart.objects.get_or_create( user = user)
    items, total = cart.remove(id)
    
    return Response([items, total]) if request.method == 'DELETE' else Response('Tell me the item to delete')


""" @login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail") """


#@login_required(login_url="login")
@api_view(['PUT'])
def cart_clear(request):
    parsed_body = json.loads(request.body)
    user  = parsed_body['user']
    cart, _ = Cart.objects.get_or_create( user = user)
    cart.items.all().delete() #untested
    return Response('The cart is empty') if request.method == 'PUT' else Response('Use put method to clear the cart.')


@login_required(login_url="login")
def cart_detail(request):
    #not yet implemented properly
    return render(request, 'cart_detail.html')