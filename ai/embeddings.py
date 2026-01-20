from pinecone import Pinecone 
from env_config import Config
from langchain_huggingface import HuggingFaceEmbeddings 
from celery import shared_task
from .pinecone import pinecone_setup
from django.core.cache import cache

# Model import and initialization
_embedding_model = None

def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = HuggingFaceEmbeddings(model_name=Config.EMBEDDINGS_MODEL_NAME)
    return _embedding_model


@shared_task
def initialize_embeddings(username, productname, productcategory, productdescription):
    
    embedding = get_embedding_model()
    vectors = embedding.embed_query(productdescription)
    print(vectors)
    
    # Temporary id
    temp_id = f"temp_{username}"
    
    # Store in pinecone
    db_data = pinecone_setup(temp_id, vectors, productname, productcategory, username)
    
    print(db_data)
    
    return db_data