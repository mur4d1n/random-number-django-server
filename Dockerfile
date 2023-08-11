FROM ubuntu:20.04

LABEL maintainer="mur4d1n@yandex.ru"
LABEL version="0.1"
LABEL description="aboba"

RUN apt update

RUN apt install -y python3 lsb-release curl gpg pip git

RUN curl -fsSL https://packages.redis.io/gpg | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

RUN echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/redis.list

RUN apt-get update

RUN apt-get install -y redis

RUN service redis-server start

RUN git clone https://github.com/mur4d1n/random-number-django-server.git

RUN cd random-number-django-server

RUN pip install Django~=4.1.4 \
redis~=4.5.1 \
channels~=4.0.0 \
asgiref~=3.6.0 \
daphne \
social-auth-app-django \
channels-redis


RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

RUN python3 manage.py runserver
