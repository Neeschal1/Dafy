from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from apps.products.models.entities import Product
from rest_framework.response import Response
from env_config import Config

def selected_product_for_similarity(selected, other):
    # For appending similar product's indexes and similar description's data
    similar_products_ids = []
    embedded_data = []
    product_ids = []
    
    try:
        products = Product.objects.values_list("Product_Description", flat=True)
    except Product.DoesNotExist:
        return Response({"Message":"Product doesnot exists. Please try again later!"})
        
    for data in other:
        embedded_data.append(data['Vector'])
        product_ids.append(data['Product_id'])
    
    # Cosine similarity and indexing
    data = cosine_similarity([selected], embedded_data)[0]
    
    # For creating a tuple for product_id and data from cosine similarity
    similarity_result = list(zip(product_ids, data))
    top_data = [(prod_id, score) for prod_id, score in similarity_result if score >= 0.1]
        
    # Sorting each of them
    sorted_data = sorted(top_data, key=lambda i: i[1], reverse=True)[1:5]
    
    for index in sorted_data:
        similar_products_ids.append(index[0])
        
    return similar_products_ids