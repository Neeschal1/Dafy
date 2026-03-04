from celery import shared_task
from django.core.cache import cache
from ai.embeddings import initialize_embeddings

@shared_task
def description_embeddings(description):
    initialize_embeddings(description)
    return