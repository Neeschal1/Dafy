from pinecone import Pinecone
from env_config import Config

pc = Pinecone(api_key=Config.PINECONE_API_KEY)
index = pc.Index(name="dafyecommerce")
