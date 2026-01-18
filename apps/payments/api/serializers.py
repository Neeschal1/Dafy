from rest_framework import serializers
from ..models.entities import Payment

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'