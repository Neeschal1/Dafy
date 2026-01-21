from ..setup import index
from ...semantic_search import selected_product_for_similarity

def fetch_products_vector(selected_product, other_products):
    selected_product_response = index.fetch(ids=[selected_product])
    other_product_response = index.fetch(ids=other_products)
    
    selected_product_data = selected_product_response.vectors[selected_product].values
    other_product_data = []
    
    for productid, vector in other_product_response.vectors.items():
        other_product_data.append({"Product_id":productid, "Vector": vector.values})
        
    return selected_product_for_similarity(selected_product_data, other_product_data)


