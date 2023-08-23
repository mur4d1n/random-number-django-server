import os

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = \
    'django-insecure-!p+*9&g&dn3k0z-i!obt2h8u#zp9$w)bor&2if!z%^=8pfas0p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '0.0.0.0',
    'server-mur4d1n.amvera.io'
]

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'randNum.apps.RandnumConfig',
    'social_django',
    'channels',
]

STATIC_DIRS = os.path.join(BASE_DIR, "static")

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'djangoProject1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends'
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoProject1.wsgi.application'

ASGI_APPLICATION = 'djangoProject1.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [f"redis://{REDIS_HOST}:{REDIS_PORT}/3"]
        },
    }
}

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication

AUTHENTICATION_BACKENDS = [
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend'
]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'
SOCIAL_AUTH_GITHUB_KEY = '1ae0326c6bb3dc2e7a5b'
SOCIAL_AUTH_GITHUB_SECRET = '537dc0c413643a5f612a3115952eaffa42d5fd9e'
