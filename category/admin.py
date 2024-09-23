from django.contrib import admin
from .models import Category
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=["catergory_name","slug"]
    list_display_links=["catergory_name"]
    list_editable=[]
    list_per_page=10
    ordering=["catergory_name"]
    prepopulated_fields={'slug':("catergory_name",)}
    
    




admin.site.register(Category,CategoryAdmin)
