from django import forms
from .models import CustomeUser


class RegisterationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter your password","class":'form-control'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm your password","class":'form-control'}))
    # email=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"test"}))



    class Meta : 
        model=CustomeUser
        fields=["email","first_name","last_name","phone_number","password"]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

#        self.fields["email"].widget.attrs["placeholder"] = 'enter your email address'

        for field in self.fields : 
            self.fields[field].widget.attrs["class"] = 'form-control'

    def clean(self):
        super().clean()
        password=self.cleaned_data["password"]
        confirm_password=self.cleaned_data["confirm_password"]
        if password != confirm_password : 
            raise forms.ValidationError("password does not match")
