from django.db import models

# Create your models here.
from store.models import Product
from store.models import Variation
class Cart (models.Model):
    cart_id=models.CharField(max_length=255,blank=True)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    is_active=models.BooleanField(default=True)
    # variation=models.ForeignKey(Variation , on_delete=models.CASCADE , null=True )
    json_variation=models.JSONField( blank=True , null=True) # all variation purchased

    def total_price_for_product(self):
        total=self.quantity * self.product.price
        return total



    


