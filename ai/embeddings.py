from pinecone import Pinecone
from env_config import Config

# Initialize pinecone API key
pc = Pinecone(api_key=Config.PINECONE_API_KEY)

print(Config.PINECONE_API_KEY)