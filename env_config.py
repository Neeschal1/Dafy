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
    
    # API key detail for AI integration
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')