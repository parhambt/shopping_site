from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.
class Color(models.Model):
    color=models.CharField(max_length=20,unique=True)
    numeric_color=models.CharField(max_length=7 , blank=True , null=True)
    def __str__(self):
        return self.color


class Size(models.Model):
    size=models.CharField(max_length=20,unique=True)
    numeric_size=models.IntegerField(blank=True , null=True)
    def __str__(self) : 
        return self.size


class Variation(models.Model):
    colors=models.ManyToManyField(Color,blank=True)
    sizes=models.ManyToManyField(Size ,blank=True)
    def __str__(self):
        return str(list(self.colors.all()))
    
    


    
class Product(models.Model):
    product_name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
    product_discriptions=models.TextField(blank=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to="phtoes/products")
    stock=models.IntegerField()
    is_availeble=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    variation=models.ForeignKey(Variation,on_delete=models.DO_NOTHING , null=True)
    def __str__(self): 
        return self.product_name
    def get_link_single_product(self):

        return reverse("info_product",kwargs={"info_product_slug":self.slug , "slug_category":self.category.slug})
    


