from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import *
from .form import *


def home(request):
    form = insertform()
    return render(request, 'home.html', {'forms':form})


def insertData(request, sname, fname, gender, clas, rno):
    try:
        data = Srecord()
        data.Sname = sname
        data.Fname = fname
        data.Gender = gender
        data.Clas = clas
        data.Rollno = rno
        data.save()
        res = "success"
    except Exception as err:
        res = err
    return JsonResponse({'response' : res})


def showData(request):
    d = Srecord.objects.all()
    data = []
    for i in d:
        dict = {'sname': i.Sname, 'fname': i.Fname, 'gender': i.Gender, 'clas': i.Clas, 'rollno': i.Rollno}
        data.append(dict)
    return JsonResponse(data, safe=False)


def showDataById(request, id):
    d = Srecord.objects.get(id=id)
    dict = {'sname': d.Sname, 'fname': d.Fname, 'gender': d.Gender, 'clas': d.Clas, 'rollno': d.Rollno}
    return JsonResponse(dict, safe=False)