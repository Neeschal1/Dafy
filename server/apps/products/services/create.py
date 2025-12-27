from apps.products.models.entities import Product

def product(validated_data):
    prodimage = validated_data['Prod_Image']
    prodname = validated_data['Prod_Name']
    prodrate = validated_data['Prod_Rate']
    
    prod = Product.objects.create(
        Prod_Image = prodimage,
        Prod_Name = prodname,
        Prod_Rate = prodrate
    )
    
    return prod

