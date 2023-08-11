from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse
from django.contrib.auth.decorators import login_required
from channels.layers import get_channel_layer
from random import randint
from time import sleep
import threading
import redis

flag = False

redis_instance = redis.StrictRedis(host="server-mur4d1n.amvera.io",
                                   port=6379, db=0)


@login_required
def index(request):
    global flag
    if not flag:
        rn = {'number': randint(0, 1000000000)}
        for key, value in rn.items():
            redis_instance.set(key, value)
        t1 = threading.Thread(target=update, daemon=True)
        t1.start()
        flag = True
    else:
        rn = {'number': redis_instance.get('number').decode()}
    return render(request, 'randNum/index.html', {'randNum': rn['number']})


def login(request):
    return render(request, 'randNum/login.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")


def update():
    while True:
        sleep(5)
        rn = {'number': randint(0, 10000000000)}
        for key, value in rn.items():
            redis_instance.set(key, value)