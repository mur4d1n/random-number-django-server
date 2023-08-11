FROM ubuntu:20.04

LABEL maintainer="mur4d1n@yandex.ru"
LABEL version="0.1"
LABEL description="aboba"

RUN apt update

RUN apt install -y python3 lsb-release curl gpg

RUN curl -fsSL https://packages.redis.io/gpg | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

RUN echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/redis.list

RUN apt-get update

RUN apt-get install redis

RUN service redis-server start


