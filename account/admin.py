from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import CustomeUser
# Register your models here.
# admin.site.register(User,)
admin.site.register(CustomeUser)