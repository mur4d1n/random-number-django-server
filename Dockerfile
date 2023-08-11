FROM ubuntu:20.04

LABEL maintainer="mur4d1n@yandex.ru"
LABEL version="0.1"
LABEL description="aboba"

RUN apt update

RUN apt install -y git

RUN git clone https://github.com/mur4d1n/random-number-django-server.git

RUN cd random-number-django-server

RUN ls
