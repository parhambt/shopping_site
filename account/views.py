from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterationForm
from django.views import View
from . models import CustomeUser
# Create your views here.
def register(request):
    form=RegisterationForm()
    context={"form":form}
    return render(request,"account/register.html",context)
class Register(View):
    def post(self,request):

        form=RegisterationForm(request.POST)
        context={'form':form}
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            password=form.cleaned_data["password"]
            phone_number=form.cleaned_data["phone_number"]
            last_name=form.cleaned_data["last_name"]
            email=form.cleaned_data["email"]
            username=email.split("@")[0]
            user=CustomeUser.objects.create_user(username=username,email=email,password=password)
            user.first_name=first_name
            user.last_name=last_name
            user.phone_number=phone_number
            user.save()
            print('valid')
            
            return render(request,"account/register.html",context)
        else : 
            print(form.errors)
            
            return render(request,"account/register.html",context)

        
    def get(self,request):
        form=RegisterationForm()
        context={"form":form}
        return render(request,"account/register.html",context)

def login(request):
    return render(request,"account/login.html")
def logout(request):
    pass