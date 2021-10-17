from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
import random
from MainApp.models import Form, Game
from django.contrib.auth.decorators import login_required
from mnc_game import settings

def games_list(request):#Список поинтеров
    f = Game.objects.filter(user=request.user, invisible = False)
    context = {"items": f}
    return render(request, 'games_list.html', context)

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




@login_required
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

@login_required
def gameeditor_save(request):#Запрос с параметрами для сохранения игры от редактора
    elm = request.POST.getlist('pointer')
    s_p=''
    for el in elm:
        s_p = s_p + el + '|'
    #print(s_p.strip('|').split('|'))
    #Все поинтеры в строку и убираем задний делимитор
    s_p = s_p.strip('|')
    #Засовываем все в таблицу

    game = Game.objects.get(game_id=request.POST['game_id'])
    game.game_name = request.POST['game_name']
    game.description = request.POST['description']
    game.inventory = request.POST['inventory']
    game.pointers = s_p
    game.user = request.user
    game.save()
    return redirect('games_list')


@login_required
def delete_game(request,param):# Удаление поинтера конкретно вместе с файлами и папками
    f = Game.objects.get(game_id=param)
    f.invisible = True
    f.save()
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

@login_required
def game_edit(request, param):#Генерация страницы редактирования игры
    ## Вся херня под динамическое создание поинтеров
    l = list()
    ids = list()
    f = Form.objects.filter(user=request.user).values('name_location', 'pointer_id')
    for elm in f:
        l.append(elm['name_location'])
        ids.append(elm['pointer_id'])
    #Тут уже начинаем от игры
    g = Game.objects.get(game_id=param)
    s =g.pointers
    s2=''
    ##А тут поинтеры которые уже были в игре
    for i, elm in enumerate(s.split('|')):
        p = Form.objects.get(pointer_id=elm)
        s2 = s2 + f'<tr id="t_t{i}"><td>Поинтер:</td><td><select name="pointer" id="" style="max-width: 300px;"><option selected value="{p.pointer_id}">{p.name_location}</option>'
        f = Form.objects.filter(user=request.user)
        for elm2 in f:
            s2 = s2 + f'<option value="{elm2.pointer_id}">{elm2.name_location}</option>'

        s2 = s2 + f'</select></td><td><input id="1" type="button" value="-" class="no_st_button_red" onclick="document.getElementById(t_t{i}.remove());"></td></tr>'
    #print(g.game_name)
    context = {"pointers": s2, "game":g, "Items": str(l).replace("'", '"'), "ids": str(ids).replace("'", '"')}
    return render(request, 'game_editor.html', context)



