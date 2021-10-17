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
from MainApp import pointers, games
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import auth


urlpatterns = [
    path('', views.index, name='base'),
    path('login', views.login_page),
    path('out',views.logout),
    path('create_pointers', pointers.create_pointers),
    path('gen_id', pointers.gen_code),
    path('game_pointers', pointers.create_game_pointers),
    path('pointers_list', pointers.pointers_list, name='pointers_list'),
    path('delete_pointer/<str:param>', pointers.delete_pointer),
    path('game_pointer_edit_save', pointers.game_pointer_edit_save),
    path('edit_pointer/<str:param>', pointers.pointer_editor),
    path('delete_files_pointer/<str:param>', pointers.delete_files_pointer),
    path('creategame_form', games.creategame_form),
    path('creategame_params', games.creategame_params),
    path('games_list', games.games_list, name='games_list'),
    path('gen_id_game', games.gen_code_game),
    path('delete_game/<str:param>', games.delete_game),
    path('game_edit/<str:param>', games.game_edit),
    path('gameeditor_save', games.gameeditor_save),
    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


