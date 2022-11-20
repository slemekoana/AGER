from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect #possibly not needed
from django.template import loader #possibly not needed
from django.contrib.auth.models import User, auth 
from django.contrib import messages
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
      #logging.basicConfig(level=logging.INFO)
      #logging.info(user)
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