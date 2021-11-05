from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from MainApp.models import Form, Teams, Game, Questions
from MainApp import games
from django.contrib.auth.decorators import login_required
from mnc_game import settings
import random


def gen_code():#Генерация кода для поинтера
    out = ''
    s = "2345789zsxecvumk" #2345789zsxecvumk
    c =1
    #c = Teams.objects.filter(team_id=out).count()
    while(c == 1):
        out=''
        for i in range(0, 11):
            iout = random.randrange(0, len(s))
            out = out + s[iout]
            #print(out)
        out = "team-" + out
        c = Teams.objects.filter(team_id=out).count()
    return out

@login_required
def create_team_form(request):
    context = {"id": gen_code(), "items":games.games(request)}
    return render(request, 'templ_create_team.html', context)

@login_required
def create_team_save(request):
    item = Teams(
        team_id=request.POST['team_id'],
        team_name=request.POST['team_name'],
        players=request.POST['players'],
        start_time=request.POST['start_time'],
        user = request.user,
        game_id = request.POST['game_id']
    )
    item.save()
    return redirect('teams_list')

@login_required
def teams_list(request):
    t = Teams.objects.filter(user=request.user, invisible=False)
    l=[]
    for elm in t:
        p = Game.objects.values_list("pointers","game_name").filter(game_id=elm.game_id)
        max = len(p[0][0].split("|"))
        c = Questions.objects.filter(game_id=elm.game_id).count()
        progress = str(c) +"/" +str(max)
        #print(progress)
        #print(p[0][1])
        d={"team_id":elm.team_id, "team_name":elm.team_name, "players":elm.players, "start_time":elm.start_time, "game_id":elm.game_id, "progress":progress, "game_name":p[0][1]}
        l.append(d)


    return render(request, 'teams_list.html', {"items":l})

@login_required
def delete_team(request,param):# Удаление команды
    f = Teams.objects.get(team_id=param)
    f.invisible = True
    f.save()
    return redirect('teams_list')

@login_required
def team_editor(request, param):
    t = Teams.objects.get(team_id=param)
    g = Game.objects.get(game_id=t.game_id)
    print(g.game_name)
    l={"team_id":t.team_id, "team_name":t.team_name, "players":t.players, "start_time":format(t.start_time,'%Y-%m-%dT%H:%M'), "game_id":t.game_id, "game_name":g.game_name}
    return render(request, 'teams_editor.html', {"Items":l})

@login_required
def editor_team_save(request):
    t = Teams.objects.get(team_id=request.POST['team_id'])
    t.players = request.POST['players']
    t.team_name = request.POST['team_name']
    t.start_time = request.POST['start_time']
    t.save()
    return redirect('teams_list')