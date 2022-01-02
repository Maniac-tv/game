"""mnc_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MainApp import views
from MainApp import pointers, games, teams, auth_algo
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import auth


urlpatterns = [
    path('adminka', auth_algo.index, name='adminka'),
    path('auth_form', auth_algo.auth_form, name='auth_form'),
    path('login', auth_algo.login_page, name="login"),
    path('out',auth_algo.logout),
    path('admin/', admin.site.urls),
    #Поинтеры
    path('create_pointers', pointers.create_pointers),
    path('gen_id', pointers.gen_code),
    path('game_pointers', pointers.create_game_pointers),
    path('pointers_list', pointers.pointers_list, name='pointers_list'),
    path('delete_pointer/<str:param>', pointers.delete_pointer),
    path('game_pointer_edit_save', pointers.game_pointer_edit_save),
    path('edit_pointer/<str:param>', pointers.pointer_editor),
    path('delete_files_pointer/<str:param>', pointers.delete_files_pointer),
    #Игры
    path('creategame_form', games.creategame_form),
    path('creategame_params', games.creategame_params),
    path('games_list', games.games_list, name='games_list'),
    path('gen_id_game', games.gen_code_game),
    path('delete_game/<str:param>', games.delete_game),
    path('game_edit/<str:param>', games.game_edit),
    path('gameeditor_save', games.gameeditor_save),
    #Команды
    path('create_team', teams.create_team_form),
    path('create_team_save', teams.create_team_save),
    path('teams_list', teams.teams_list, name='teams_list'),
    path('delete_team/<str:param>',teams.delete_team),
    path('team_edit/<str:param>', teams.team_editor),
    path('editor_team_save', teams.editor_team_save),
    #Работа с игроками
    path('player_get_game', views.player_prev),
    path('', views.player_get_code),
    path('check_login',views.check_login)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


