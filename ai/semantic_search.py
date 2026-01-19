from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from apps.products.models.entities import Product
from rest_framework.response import Response
from env_config import Config

embedding = 1


def selected_product(about_product):
    # For appending similar product's indexes and similar description's data
    indexed_details = []
    similar_products_description = []
    
    try:
        products = Product.objects.values_list("Product_Description", flat=True)
    except Product.DoesNotExist:
        return Response({"Message":"Product doesnot exists. Please try again later!"})
    
    # Embeddings of both, particular description and whole product's description
    whole_data_query = embedding.embed_documents(products)
    single_data_query = embedding.embed_query(about_product)
    
    # Cosine similarity and indexing
    data = cosine_similarity([single_data_query], whole_data_query)[0]
    for index, detail in enumerate(data):
        indexed_details.append((index, detail))
        
    # Sorting each of them
    sorted_data = sorted(indexed_details, key=lambda i: i[1], reverse=True)[1:4]
    
    # Similar Products
    for index in sorted_data:
        similar_products_description.append(products[index[0]])
    
    return similar_products_description
