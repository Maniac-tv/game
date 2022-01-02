from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from mnc_game import settings
from django.contrib import auth

def auth_form(request):
    return render(request, 'auth_form.html')

def login_page(request):
   if request.method == 'POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       print("username =", username)
       print("password =", password)
       User = auth.authenticate(request, username=username, password=password)
       print(User)
       if User is not None:
           auth.login(request, User)
           return redirect('adminka')
       else:
           # Return error message
           print('Error')
           s = '<center>The Dick!<br/><img src="static/imgs/haiz.jpg" height="800" wedth="1100"></center>'
           return render(request, 'auth_form.html', {"items":"Error"})
   return render(request, 'adminka')


def logout(request):#Логаут ясен буй
    auth.logout(request)
    return index(request) #render(request, 'body.html')

def index(request):#Базовая страница
    return render(request, 'body.html')