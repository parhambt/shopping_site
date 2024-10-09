from django.db import models
from account.models import CustomeUser
from store.models import Product ,Variation
# Create your models here.
class Payments(models.Model):
    user=models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    payment_id=models.CharField(max_length=100)
    payment_method=models.CharField(max_length=100)
    amount_paid=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.payment_id


class Order(models.Model):
    STATUS= (
        ("New","New"),
        ('Accepted','Accepted'),
        ("Completed","Completed"),
        ("Canceled","Canceled"),
    )
    user=models.ForeignKey(CustomeUser,on_delete=models.SET_NULL, null=True)
    payment=models.ForeignKey(Payments,on_delete=models.SET_NULL, null=True,blank=True)

    order_number=models.CharField(max_length=20 , unique=True) # uniqe one

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=60)
    address_line_1=models.CharField(max_length=100)
    address_line_2=models.CharField(max_length=100,blank=True)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    order_note=models.TextField(max_length=300 , blank=True)
    
    order_total=models.FloatField()
    tax=models.FloatField()
    status=models.CharField(max_length=10,choices=STATUS,default="New")
    ip=models.CharField(max_length=20,blank=True)
    is_orderd=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def full_address(self):
        return f"{self.address_line_1} {self.address_line_2}"
    def __str__(self):
        return self.first_name

class OrderProduct(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    payment=models.ForeignKey(Payments,on_delete=models.SET_NULL, null=True,blank=True)
    user=models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variation=models.ForeignKey(Variation,on_delete=models.CASCADE)
    color=models.CharField(max_length=20)
    size=models.CharField(max_length=20)
    quantity=models.IntegerField()
    product_price=models.FloatField()
    ordered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product.product_name



    
    





