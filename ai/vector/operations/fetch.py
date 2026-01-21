# from ..setup import index

# def fetch_products_vector(tempid):
#     response = index.fetch(ids=[tempid])
#     print(response)
#     return

# fetch_products_vector()


from ..setup import index

def fetch_products_vector(selected_product, other_products):
    selected_product_response = index.fetch(ids=[selected_product])
    other_product_response = index.fetch(ids=[other_products])
    
    # For selected product
    selected_product_data = selected_product_response.vectors[selected_product].values
    other_product_data = []
    
    for productid, vectors in other_product_response.vectors.items():
        other_product_data.append({productid, vectors})
    
    return other_product_data

fetch_products_vector()