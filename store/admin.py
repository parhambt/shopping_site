from django.contrib import admin
from .models import Product ,Color ,Size ,Variation , ReviewRaiting ,ProductGallery
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.html import format_html



class ProductGalleryInlineAdmin(admin.TabularInline):

    model=ProductGallery
    extra=1

    

    
class ProductAdmin(admin.ModelAdmin):
    list_display=["product_name","price","stock","category","modified_date","is_availeble",'variation']
    ordering=["-modified_date"]
    prepopulated_fields={"slug":["product_name",]}
    inlines=[ProductGalleryInlineAdmin]




admin.site.register(Product,ProductAdmin)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Variation)
admin.site.register(ReviewRaiting)
admin.site.register(ProductGallery)
