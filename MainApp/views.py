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



@login_required
def creategame_form(request):#Страница создания игры
    #print('game')
    l = list()
    ids = list()
    f = Form.objects.filter(user=request.user).values('name_location','pointer_id')
    for elm in f:
        l.append(elm['name_location'])
        ids.append(elm['pointer_id'])

    context = {"Items": str(l).replace("'",'"'),"ids": str(ids).replace("'",'"')}
    #print(context)
    return render(request, 'templ_create_game.html', context)

def creategame_params(request):#Запрос с параметрами для создания игры
    elm = request.POST.getlist('pointer')
    s_p=''
    for el in elm:
        s_p = s_p + el + '|'
    #print(s_p.strip('|').split('|'))
    #Все поинтеры в строку и убираем задний делимитор
    s_p = s_p.strip('|')
    #Засовываем все в таблицу
    game = Game(game_id=request.POST['game_id'], game_name=request.POST['game_name'], description=request.POST['description'], inventory=request.POST['inventory'], pointers=s_p, user=request.user)
    game.save()
    return redirect('games_list')

def games_list(request):#Список поинтеров
    f = Game.objects.filter(user=request.user)
    context = {"items": f}
    return render(request, 'games_list.html', context)

def delete_game(request,param):# Удаление поинтера конкретно вместе с файлами и папками
    f = Game.objects.get(game_id=param)
    f.delete()
    return redirect('games_list')


@login_required
def gen_code_game(request):#Генерация кода для поинтера
    out = ''
    s = "2345789zsxecvumk" #2345789zsxecvumk
    c =1
    #c = Form.objects.filter(pointer_id=out).count()
    while(c == 1):
        out=''
        for i in range(0, 11):
            iout = random.randrange(0, len(s))
            out = out + s[iout]
        #print(out)
        out = "gme-" + out
        c = Game.objects.filter(game_id=out).count()
    return HttpResponse(out)





