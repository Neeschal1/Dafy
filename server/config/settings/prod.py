from .base import *

DEBUG = False
ALLOWED_HOSTS = []

# Default Database (Postgre SQL) : For production
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