from pathlib import Path
from .base import *
from env_config import Config

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Debug: ready for production
DEBUG = False
SECRET_KEY = Config.SECRET_KEY

# Root URL to hit, i. e. url of project of an entire application
ROOT_URLCONF = 'config.urls'

# Allowed hosts to access this backend system
ALLOWED_HOSTS = ['*']

# Web server gateway interface initialization
WSGI_APPLICATION = 'server.config.wsgi.application'

# PostgreSQL Database (For production level)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydatabase",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
