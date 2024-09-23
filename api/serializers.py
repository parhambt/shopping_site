from rest_framework import serializers
from store.models import Product

class ProductSerializer(serializers.ModelSerializer) : 
    class Meta  :
        model=Product
        fields=["product_name","product_discriptions","price","category"]
        
