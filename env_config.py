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