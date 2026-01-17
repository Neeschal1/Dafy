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

# Asynchronous server gateway interface initialization
ASGI_APPLICATION = 'config.asgi.application'

# PostgreSQL Database (For production level)
DATABASES = {
    "default": {
        "ENGINE": Config.ENGINE,
        "NAME": Config.NAME,
        "USER": Config.USER,
        "PASSWORD": Config.PASSWORD,
        "HOST": Config.HOST,
        "PORT": Config.PORT,
    }
}
