from ..setup import index
from .fetch import fetch_products_vector

def pinecone_setup(tempid, vectors, productname, productcategory, username):
    index.upsert(
        vectors=[
            {
                "id": tempid,
                "values": vectors,
                "metadata": {
                    "product_name": productname,
                    "product_category": productcategory,
                    "username": username,
                    "status": "pending",
                },
            }
        ]
    )
    
    fetch_products_vector(tempid)

    return {"status": "success", "vector_id": tempid}
