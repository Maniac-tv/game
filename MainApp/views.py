from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
import random
from mnc_game import settings
from django.core.files.storage import FileSystemStorage
from MainApp.models import Form, Game
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_page(request):
   if request.method == 'POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       print("username =", username)
       print("password =", password)
       User = auth.authenticate(request, username=username, password=password)
       if User is not None:
           auth.login(request, User)
           return redirect('/')
       else:
           # Return error message
           s = '<center>The hui!<br/><img src="static/imgs/haiz.jpg" height="800" wedth="1100"></center>'
           return HttpResponse(s)
   #return render(request, '/')


def logout(request):#Логаут ясен буй
    auth.logout(request)
    return index(request) #render(request, 'body.html')

def index(request):#Базовая страница
    return render(request, 'body.html')






