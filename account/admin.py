from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import CustomeUser
# Register your models here.
# admin.site.register(User,)
class CustomeUserAdomin(admin.ModelAdmin):
    list_display=["email","username","date_joined","last_login","is_active","is_superuser"]
    list_editable=["is_active","is_superuser"]
    ordering=["-date_joined"]
admin.site.register(CustomeUser,CustomeUserAdomin)