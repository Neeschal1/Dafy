from pathlib import Path
from .base import *
from env_config import Config


# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Debug: False when it comes to production
DEBUG = True
SECRET_KEY = Config.SECRET_KEY


# Allowed hosts to access this backend system
ALLOWED_HOSTS = ['*']


# Root URL to hit, i. e. url of project of an entire application
ROOT_URLCONF = 'config.urls'


# Asynchronous server gateway interface initialization
ASGI_APPLICATION = 'config.asgi.application'


# Redis cache setting 
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}


# Celery setup
CELERY_BROKER_URL = "redis://127.0.0.1:6379"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_WORKER_POOL = "solo"


# Default Database (Only while it is in developmental state)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
