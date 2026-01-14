from pathlib import Path
from .base import *
from env_config import Config

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Debug: False when it comes to production
DEBUG = True
SECRET_KEY = Config.SECRET_KEY

# Root URL to hit, i. e. url of project of an entire application
ROOT_URLCONF = 'config.urls'

# Allowed hosts to access this backend system
ALLOWED_HOSTS = ['*']

# Web server gateway interface initialization
WSGI_APPLICATION = 'server.config.wsgi.application'

# Default Database (Only while it is in developmental state)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
