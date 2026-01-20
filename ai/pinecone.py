from pinecone import Pinecone
from env_config import Config

pc = Pinecone(api_key=Config.PINECONE_API_KEY)
index = pc.Index(name="dafyecommerce")

def pinecone_setup(tempid, vectors, productname, productcategory, username):
    db_details = index.upsert(
        vectors=[{
            "id": tempid,
            "values": vectors,
            "metadata": {
                "product_name": productname,
                "product_category": productcategory,
                "username": username,
                "status": "pending"
            }}]
    )
    return db_details