from pinecone import Pinecone 
from env_config import Config
from langchain_huggingface import HuggingFaceEmbeddings 
from celery import shared_task
from .vector.operations.upsert import pinecone_setup
from django.core.cache import cache
import random
import string

# Model import and initialization
_embedding_model = None


# For unique temp id in every new attempt
def unique_id():
    numbers = string.digits
    words = string.ascii_letters
    new_id = ""
    length = 10
    for _ in range(length):
        random_number = random.choice(numbers)
        random_word = random.choice(words)
        new_id = new_id + random_number + random_word
        if len(new_id) == length:
            break
    return new_id


# Model setup
def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = HuggingFaceEmbeddings(model_name=Config.EMBEDDINGS_MODEL_NAME)
    return _embedding_model


@shared_task
def initialize_embeddings(username, productname, productcategory, productdescription):
    embedding = get_embedding_model()
    vectors = embedding.embed_query(productdescription)
    
    # Temporary id
    unique_number = unique_id()
    temp_id = f"temp_{username}_{unique_number}"
    
    print(vectors)
    print(temp_id)
    
    # Store in pinecone
    db_data = pinecone_setup(temp_id, vectors, productname, productcategory, username)
    print(db_data)
    return db_data
