from django import forms
from .models import ReviewRaiting
class ReviewForms(forms.ModelForm) : 
    class Meta : 
        model=ReviewRaiting
        fields =["subject","review","rating"]