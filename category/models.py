from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    catergory_name=models.CharField(max_length=50 , unique=True)
    slug=models.SlugField(max_length=100 , unique=True)
    description=models.TextField(blank=True )
    catergory_images=models.ImageField(upload_to="phtoes/category",blank=True)
    def __str__(self):
        return self.catergory_name
    def get_url_product_by_category(self):
        url=reverse("product_by_category",args=[self.slug])
        return url
