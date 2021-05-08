from django.shortcuts import render, HttpResponse
import random

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



