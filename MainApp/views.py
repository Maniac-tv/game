from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
import random
import shutil
from MainApp.models import Form
import os
from mnc_game import settings
from django.core.files.storage import FileSystemStorage
from MainApp.models import Form
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

def create_pointers(request):#Страница создания поинтера
    return render(request, 'templ_create_pointers.html')

@login_required
def creategame_form(request):#Страница создания игры
    #print('game')
    l = list()
    f = Form.objects.filter(user=request.user).values('name_location')
    for elm in f:
        l.append(elm['name_location'])
    context = {"Items": str(l).replace("'",'"')}
    #print(context)
    return render(request, 'templ_create_game.html', context)

def creategame_params(request):#Страница создания игры
    print(request.POST)
    return 0

def pointers_list(request):#Список поинтеров
    f = Form.objects.filter(user=request.user)
    context = {"items": f}
    return render(request, 'pointer_list.html', context)

@login_required
def gen_code(request):#Генерация кода для поинтера
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
        out = "mnc-" + out
        c = Form.objects.filter(pointer_id=out).count()
    return HttpResponse(out)

@login_required
def create_game_pointers(request):#Сохранение поинтера
    item = Form(pointer_id=request.POST['pointer_id'], lat=request.POST['lat'], long=request.POST['long'], name_location=request.POST['name_location'], description=request.POST['description'], help=request.POST['help'], answer=request.POST['answer'], area=request.POST['area'], user=request.user)
    item.save()
    #Если есть файлы создаем папку с названием идентификатора и сохраняем туда
    if 'my_file' in request.FILES:
        os.mkdir(os.path.join(settings.MEDIA_ROOT, request.POST['pointer_id']))
        f = request.FILES.getlist('my_file')
        for elm in f:
            fs = FileSystemStorage()
            filename = fs.save(os.path.join(os.path.join(settings.MEDIA_ROOT, request.POST['pointer_id']), elm.name), elm)
    return redirect('pointers_list')

@login_required
def game_pointer_edit_save(request):# Запрос на сохранение отредактированного поинтера
    f = Form.objects.get(pointer_id=request.POST['pointer_id'])
    f.lat = request.POST['lat']
    f.long = request.POST['long']
    f.name_location = request.POST['name_location']
    f.description=request.POST['description']
    f.help = request.POST['help']
    f.answer = request.POST['answer']
    f.area = request.POST['area']
    f.user = request.user
    f.save()
    f = request.FILES.getlist('my_file')
    for elm in f:
        fs = FileSystemStorage()
        filename = fs.save(os.path.join(os.path.join(settings.MEDIA_ROOT, request.POST['pointer_id']), elm.name), elm)
    return redirect('pointers_list')

def delete_pointer(request,param):# Удаление поинтера конкретно вместе с файлами и папками
    f = Form.objects.get(pointer_id=param)
    f.delete()
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, param), ignore_errors=True)
    print(os.path.join(settings.MEDIA_ROOT, param))
    return redirect('pointers_list')

@login_required
def pointer_editor(request, param):#Форма для редактирования поинтера
    i_list = list()
    i_list.append('LTE')
    i_list.append('3G')
    i_list.append('Так себе')
    i_list.append('Бункер/Пустыня')
    f = Form.objects.get(pointer_id=param)
    area_list=''
    for elm in i_list:
        if elm == f.area:
            area_list = area_list + f'<option selected value="{elm}">{elm}</option>'
        else:
            area_list = area_list + f'<option value="{elm}">{elm}</option>'

    fl = file_list(os.path.join(settings.MEDIA_ROOT, param))
    #print(f.__doc__)
    context = {"Items" : f,"Files":fl, 'Area':area_list}
    #print(context)
    return render(request, 'pointer_editor.html', context)

def file_list(path):#Возвращает список файлов
    if os.path.exists(path):
        files = os.listdir(path)
    #print(files)
        return files

def delete_files_pointer(request,param):# Удаление файлов поинтера по одному из формы редактирования поинтера, и возврат оставшихся файлов
    s2=''
    param = param.replace('|', '/')
    os.remove(os.path.join(settings.MEDIA_ROOT, param))
    #print(os.path.join(settings.MEDIA_ROOT, param))
    id_p = param.split('/')[0] # Получаем идентификатор поинтера
    #print('id_p=',id_p)
    t = file_list(os.path.join(settings.MEDIA_ROOT, id_p)) #Получаем список оставшихся файлов в папке поинтера
    #print(t)
    #Формируем ответ из списка файлов
    for elm in t:
        s = '''<tr><td style="text-align:right;"></td><td>'''+elm+'''<a onclick="get('delete_files_pointer/'''+id_p+'''|'''+elm+'''','#files')" href="#" title="Удалить конкретно"><svg xmlns="http://www.w3.org/2000/svg" color = "Red" width="16" height="16" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16"><path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/></svg></a></td> </tr>'''
        s2 = s2 + s
    return HttpResponse(s2)




