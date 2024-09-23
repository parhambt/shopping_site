from django import forms
from django.contrib.auth.models import User


class RegisterationForm(forms.ModelForm):
    class Meta : 
        model=User
        fields=['name',"lastname"]
