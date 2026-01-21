from pinecone import Pinecone
from env_config import Config
from apps.products.models.entities import Product

pc = Pinecone(api_key="pcsk_4G8kWh_HnrQs4a7T8ujpyC7ip28rSB41KXrJVtTWNBhcHjgcjzwKPhtFmY4h4LHTep4BFV")
index = pc.Index(name="dafyecommerce")

def fetch_products_vector(tempid1, tempid2):
    # productids = []
    # data = Product.objects.all()
    # for products in data:
    #     ids = products.Product_ID
    #     productids.append(ids)
    # return productids
    temp = index.fetch(ids=[tempid1, tempid2])
    for productid, vector in temp.vectors.items():
        print(productid)
        print(vector.values)

data = fetch_products_vector("temp_vrikshya_9I5X7l0E4U", "temp_asmita_temp_asmita_7i7W0R6h2g")
