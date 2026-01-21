from ..setup import index
from ...semantic_search import selected_product

def fetch_products_vector(selected_product, other_products):
    selected_product_response = index.fetch(ids=[selected_product])
    other_product_response = index.fetch(ids=other_products)
    
    selected_product_data = selected_product_response.vectors[selected_product].values
    other_product_data = []
    
    for productid, vector in other_product_response.vectors.items():
        other_product_data.append({"Product_id":productid, "Vector": vector.values})
        
    # print(f"Selected Product responses: {selected_product_response}")
    # print(f"Other Product responses: {other_product_response}")
    print("Length of data: ", len(other_product_data),"Other Products Data:\n", other_product_data)
    return selected_product_data


    # similar_products = selected_product(selected_product_data, other_product_data)
