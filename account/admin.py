from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import CustomeUser ,UserProfile
from django.utils.html import format_html
# Register your models here.
# admin.site.register(User,)
class CustomeUserAdomin(admin.ModelAdmin):
    list_display=["email","username","date_joined","last_login","is_active","is_superuser"]
    list_editable=["is_active","is_superuser"]
    ordering=["-date_joined"]
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html(f'<img src={object.profile_picture.url} width="30" style="border-radius:50%;">')
    
    thumbnail.short_description = "Profile_Picture"
    list_display=["user","city","state","country","thumbnail"]
    
admin.site.register(CustomeUser,CustomeUserAdomin)
admin.site.register(UserProfile,UserProfileAdmin)