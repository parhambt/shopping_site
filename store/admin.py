from django.contrib import admin
from .models import Product ,Color ,Size ,Variation , ReviewRaiting
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=["product_name","price","stock","category","modified_date","is_availeble",'variation']
    ordering=["-modified_date"]
    prepopulated_fields={"slug":["product_name",]}



admin.site.register(Product,ProductAdmin)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Variation)
admin.site.register(ReviewRaiting)
