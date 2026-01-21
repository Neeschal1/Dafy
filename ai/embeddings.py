from pinecone import Pinecone 
from env_config import Config
from langchain_huggingface import HuggingFaceEmbeddings 
from celery import shared_task
from celery.signals import worker_process_init
from .vector.operations.upsert import pinecone_setup

# Model import and initialization
_embedding_model = None

@worker_process_init.connect
def init_worker_process(sender=None, **kwargs):
    global _embedding_model
    _embedding_model = HuggingFaceEmbeddings(model_name=Config.EMBEDDINGS_MODEL_NAME)
    print("Model loaded on worker startup!")

# Model setup
def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = HuggingFaceEmbeddings(model_name=Config.EMBEDDINGS_MODEL_NAME)
    return _embedding_model

@shared_task
def initialize_embeddings(username, productname, productcategory, productdescription, temp_id):
    embedding = get_embedding_model()
    vectors = embedding.embed_query(productdescription)
    
    # Store in pinecone
    db_data = pinecone_setup(temp_id, vectors, productname, productcategory, username)
    return db_data
