from django.shortcuts import render, HttpResponse
import random
from MainApp.models import Form
import os
from mnc_game import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request,'body.html')

def create_pointers(request):
    return render(request, 'create_pointers.html')

def gen_code(request):
    out=''
    s= "2345789zsxecvumk"
    for i in range(0,11):
        iout = random.randrange(0,len(s))
        out = out + s[iout]
    out = "mnc-"+out
    return HttpResponse(out)

def game_pointers(request):
    print(request.POST['pointer_id'])
    item = Form(pointer_id=request.POST['pointer_id'], lat=request.POST['lat'], lang=request.POST['lang'], name_location=request.POST['name_location'], description=request.POST['description'], help=request.POST['help'], area=request.POST['area'])
    item.save()
    #Если есть файлы создаем папку с названием идентификатора и сохраняем туда
    if 'my_file' in request.FILES:
        os.mkdir(os.path.join(settings.MEDIA_ROOT, request.POST['pointer_id']))
        f = request.FILES.getlist('my_file')
        for elm in f:
            fs = FileSystemStorage()
            filename = fs.save(os.path.join(os.path.join(settings.MEDIA_ROOT, request.POST['pointer_id']),elm.name), elm)

    return HttpResponse(f'<script>alert(\'Создан поинтер {request.POST["pointer_id"]} с названием {request.POST["name_location"]}\')</script>')



