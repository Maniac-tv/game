from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
import random
from mnc_game import settings
from django.core.files.storage import FileSystemStorage
from MainApp.models import Form, Teams, Game, Questions,game_user
from django.contrib import auth
import datetime
from django.db.models.functions import Length, Upper
import pytz




def player_prev(request):
    if Teams.objects.filter(game_code=request.POST.get("game_code").upper()).count() > 0:
        t = Teams.objects.get(game_code=request.POST.get("game_code").upper())
        g = Game.objects.get(game_id=t.game_id)
        l = {"description": g.description, "inventory": g.inventory, "start_time": t.start_time, "players": t.players}
        #print(t.start_time.replace(tzinfo=pytz.UTC) < datetime.datetime.now().replace(tzinfo=pytz.UTC))
        if t.start_time.replace(tzinfo=pytz.UTC) < datetime.datetime.now().replace(tzinfo=pytz.UTC):
            l.update({"button":"True"})
        return render(request,"templ_prev_game.html", {"Items":l})
    else:
        return HttpResponse("Invalid code!")

def check_login(request):
    user = game_user.objects.filter(user_name__iexact = request.POST.get("game_nick"))
    if len(user) > 0:
        return HttpResponse("User name is exists!")
    else:
        g_u = game_user(user_name = request.POST.get("game_nick"), user_id = request.POST.get("csrfmiddlewaretoken"), team_id = "", user_ip = request.META.get('REMOTE_ADDR'), user_active = True )
        g_u.save()
        return render(request,"templ_user_form.html")

def player_get_code(request):
    return render(request, 'player_get_code.html')