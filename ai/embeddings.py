from pinecone import Pinecone
from env_config import Config
from langchain_huggingface import HuggingFaceEmbeddings
from celery import shared_task
from django.core.cache import cache

# Initialize pinecone API key
pc = Pinecone(api_key=Config.PINECONE_API_KEY)
index = pc.Index("dafy")


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
    vector = embedding.embed_query(productdescription)
    print(vector)
    
    # Temporary id
    temp_id = f"temp_{username}"
    
    # Store in pinecone
    db = index.upsert(vectors=[{
        "id": temp_id,
        "values": vector,
        "metadata": {
            "product_name": productname,
            "product_category": productcategory,
            "username": username,
            "status": "pending"
        }
    }])
    
    print(db)
    
    return db