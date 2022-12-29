from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.contrib.auth.decorators import login_required
from random import randint
from time import sleep
from .models import RandNum
import threading

flag = False


@login_required
def index(request):
    global flag
    if not flag:
        rn = RandNum(randNum=randint(0, 10000000000))
        rn.save()
        t1 = threading.Thread(target=update, daemon=True)
        t1.start()
        flag = True
    randNum = RandNum.objects.get(id=1).randNum
    return render(request, 'randNum/index.html', {'randNum': randNum})


def login(request):
    return render(request, 'randNum/login.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")


def update():
    while True:
        sleep(5)
        rn = RandNum.objects.get(id=1)
        rn.randNum = randint(0, 10000000000)
        rn.save()
        JsonResponse({'new_num': rn.randNum})
