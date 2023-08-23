import threading
import redis

from random import randint
from time import sleep

from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required


flag = False

redis_instance = redis.StrictRedis(host="127.0.0.1",
                                   port=6379, db=0)


@login_required
def index(request):
    global flag
    if not flag:
        pass
    else:
        rn = {'number': redis_instance.get('number').decode()}
    return render(request, 'randNum/index.html', {'randNum': rn['number']})


def login(request):
    return render(request, 'randNum/login.html')


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")


def update():
    while True:
        sleep(5)
        rn = {'number': randint(0, 10000000000)}
        for key, value in rn.items():
            redis_instance.set(key, value)


if __name__ == '__main__':
    rn = {'number': randint(0, 1000000000)}
    for key, value in rn.items():
        redis_instance.set(key, value)
    t1 = threading.Thread(target=update, daemon=True)
    t1.start()
    flag = True