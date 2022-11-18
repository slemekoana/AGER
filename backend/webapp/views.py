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
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    password2 = request.POST["password2"]
    if password == password2:
      #we check if the email already exist in the User database
      if email and User.objects.filter(email = email ).exists():
        messages.info(request, "Email already used.")
        return redirect('register') #same as HttpResponseRedirect
      elif User.objects.filter(username = username ).exists():
        messages.info(request, "Username already used.")
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return  redirect('login')
    else:
      messages.info(request, "Passwords don't match.")
  else: 
    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))

def login(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]

    user = auth.authenticate(username=username, password = password)
    if user is not None:
      auth.login(request, user) #auth does all the work for authentification in the User database from admin
      #logging.basicConfig(level=logging.INFO)
      #logging.info(user)
      return redirect('/')
    else:
      messages.info(request, "Invalid Credentials")
      return redirect("login")
  else:
    return render(request, "login.html")

def logout(request):
  auth.logout(request)
  return redirect('/')