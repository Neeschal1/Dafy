from ..models.entities import Product
from rest_framework.response import Response

def other_similar_products(similar_products, selected_product, prod, user):
    same_products = []
    for prod_id in similar_products:        
        try:
            same_prods = Product.objects.get(Product_ID = prod_id)
        except Product.DoesNotExist:
            return Response({"Message":"Product doesnot exists. Come... Visit soon to fetch more ones. Thank you!"})
        same_products.append({
            "Product Name": same_prods.Product_Name,
            "Product Id": same_prods.Product_ID,
            "Product Category": same_prods.Product_Category,
            "Product Description": same_prods.Product_Description,
            "Images":{
                    "Image one": same_prods.Image_one,
                    "Image two": same_prods.Image_two,
                    "Image three": same_prods.Image_three,
                    "Image four": same_prods.Image_four,
                    "Image five": same_prods.Image_five,
                },
            "Other Detail": {
                    "Seller name": user.first_name,
                    "Price": same_prods.Price,
                    "Product's bought date by the seller": same_prods.Bought_Date,
                }
            })
        
    return Response({"Message": {
            "Your Selected Product": {
                "Product Id": selected_product,
                "Product Name": prod.Product_Name,
                "Product Category": prod.Product_Category,
                "Product Description": prod.Product_Description,
                "Images":{
                    "Image one": prod.Image_one,
                    "Image two": prod.Image_two,
                    "Image three": prod.Image_three,
                    "Image four": prod.Image_four,
                    "Image five": prod.Image_five,
                },
                "Other Detail": {
                    "Seller name": user.first_name,
                    "Price": prod.Price,
                    "Product's bought date by the seller": prod.Bought_Date,
                }
            },
           "Other similar products": same_products
        }})