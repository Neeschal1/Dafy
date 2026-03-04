import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    # Secret key of project
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    
    # Database details
    ENGINE = os.getenv('ENGINE')
    NAME = os.getenv('NAME')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    
    
    # Celery details
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    
    
    # API key detail for AI integration
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    GROQ_MODEL_NAME = os.getenv('GROQ_MODEL_NAME')
    GROQ_MODEL_PROVIDER = os.getenv('GROQ_MODEL_PROVIDER')
    
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    GOOGLE_MODEL_NAME = os.getenv('GOOGLE_MODEL_NAME')
    GOOGLE_MODEL_PROVIDER = os.getenv('GOOGLE_MODEL_PROVIDER')
    
    MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
    MISTRAL_MODEL_NAME = os.getenv('MISTRAL_MODEL_NAME')
    MISTRAL_MODEL_PROVIDER = os.getenv('MISTRAL_MODEL_PROVIDER')
    
    
    # Embeddings model
    EMBEDDINGS_MODEL_NAME = os.getenv('EMBEDDINGS_MODEL_NAME')
    
    
    # Pinecone API Key (For vector database)
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    
    
    # Stripe Payment Gateway Integration Details
    STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')