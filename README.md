# random-number-django-server

Это приложение реализует веб-сервер на фреймворке Django, возвращающий страницу с динамически генерируемым на сервере случайным числом, единым для всех сессий, и авторизацией через Github

Для локального деплоя необходимо:

  1. Установить Redis
  1. Установить зависимости:
```
pip install -r requirements.txt
```
  1. Запустить веб-сервер командой:
```
python3 manage.py runserver
```
  
По умолчанию сервер доступен по адресу 127.0.0.1:8000
