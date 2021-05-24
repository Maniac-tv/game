from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
import random
from MainApp.models import Form
import os
from mnc_game import settings
from django.core.files.storage import FileSystemStorage
from MainApp.models import Form

# Create your views here.

def index(request):#Базовая страница
    return render(request,'body.html')

def create_pointers(request):#Страница создания поинтера
    return render(request, 'create_pointers.html')

def pointers_list(request):#Список поинтеров
    f = Form.objects.all()
    context = {"items": f}

    return render(request, 'pointer_form.html',context)

def gen_code(request):#Генерация кода для поинтера
    out=''
    s= "2345789zsxecvumk"
    for i in range(0,11):
        iout = random.randrange(0,len(s))
        out = out + s[iout]
    out = "mnc-"+out
    return HttpResponse(out)

def game_pointers(request):#Сохранение поинтера
    print(request.POST['pointer_id'])
    item = Form(pointer_id=request.POST['pointer_id'], lat=request.POST['lat'], long=request.POST['long'], name_location=request.POST['name_location'], description=request.POST['description'], help=request.POST['help'], answer=request.POST['answer'], area=request.POST['area'])
    item.save()
    #Если есть файлы создаем папку с названием идентификатора и сохраняем туда
    if 'my_file' in request.FILES:
        os.mkdir(os.path.join(settings.MEDIA_ROOT, request.POST['pointer_id']))
        f = request.FILES.getlist('my_file')
        for elm in f:
            fs = FileSystemStorage()
            filename = fs.save(os.path.join(os.path.join(settings.MEDIA_ROOT, request.POST['pointer_id']),elm.name), elm)
    return HttpResponse(f'<script>alert(\'Создан поинтер {request.POST["pointer_id"]} с названием {request.POST["name_location"]}\')</script>')

def delete_pointer(request,param):
    f = Form.objects.get(pointer_id=param)
    f.delete()
    return redirect('pointers_list')



