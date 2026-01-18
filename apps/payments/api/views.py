from .serializers import PaymentSerializers
from rest_framework.views import APIView
from env_config import Config
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..models.entities import Payment
from rest_framework.response import Response
import stripe

stripe.api_key = Config.STRIPE_SECRET_KEY


class PaymentSerializersView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        paid = PaymentSerializers(data=request.data)
        paid.is_valid(raise_exception=True)

        Productname = paid.validated_data["Product_Name"]
        Productdescription = paid.validated_data["Product_Description"]
        Productimage = paid.validated_data["Product_Image"]
        Priceofproduct = paid.validated_data["Price"]

        try:
            lineitem = [
                {
                    "quantity": 1,
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(Priceofproduct * 100),
                        "product_data": {
                            "name": Productname,
                            "description": Productdescription,
                            "images": [Productimage]
                        },
                    },
                }
            ]
            checkout_session = stripe.checkout.Session.create(
                line_items=lineitem,
                mode='payment',
                success_url="https://www.pinterest.com/pin/316729786314156192/",
                cancel_url="https://www.pinterest.com/pin/1125968651884142/"
            )
        except Exception as e:
            return Response({"Message":"Exception Occured!", "Issue":str(e)})
        
        pay = Payment.objects.create(
            Buyers_Name = paid.validated_data["Buyers_Name"],
            Buyers_Username = paid.validated_data["Buyers_Username"],
            Product_Name = Productname,
            Product_Description = Productdescription,
            Product_Image = Productimage,
            Product_Category = paid.validated_data["Product_Category"],
            Price = Priceofproduct,
            Paid = True
        )

        return Response({"Message":"Payment Created.", "Buyer's Detail": {
            "Product Name": pay.Product_Name,
            "Product Description": pay.Product_Description,
            "Product Price": pay.Price,
            }, "URL":checkout_session.url})
