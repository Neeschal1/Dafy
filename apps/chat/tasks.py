from celery import shared_task
from django.core.cache import cache

    
@shared_task
def side_task():
    data = []
    for _ in range(5000):
        print(_)
        data.append("Hi, from redis celery!")
    cache.set("celerydata", data, timeout=600)
    return 