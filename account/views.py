from django.shortcuts import render ,redirect
from django.http import HttpResponse 
from .forms import RegisterationForm
from django.views import View
from . models import CustomeUser
from django.contrib import messages , auth 

# Create your views here.

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
            messages.success(request,"registration is success")
            
            return redirect('register')
        else : 
            print(form.errors)
            
            return render(request,"account/register.html",context)

        
    def get(self,request):
        form=RegisterationForm()
        context={"form":form}
        return render(request,"account/register.html",context)


    
def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')    
        user=auth.authenticate(request=request,email=email,password=password)
        if user  is not None  :
            auth.login(request=request,user=user)
            
            # messages.success(request,"authentication is succseed")
            return redirect("store_view")
        else : 
            messages.error(request,"Error : authentication is failed")
            return redirect("login")
    
    elif request.method == "GET" : 
        return render(request,"account/login.html")


      
def logout(request):
    user=request.user
    if user.is_authenticated  :
        auth.logout(request)
        messages.success(request,"you are succsesfully looged out")
        return redirect("login")
    else  :
        pass





# class Login(View):

#     def get(self,request):
#         return render(request,"account/login.html")
        
#     def post(self,request):
#         email=request.POST.get('email')
#         password=request.POST.get('password')

#         user=auth.aauthenticate(email=email, password=password)
#         if user  is not None  :
#             auth.login(request=request,user=user)
            
#             # messages.success(request,"authentication is succseed")
#             return redirect("store_view")
#         else : 
#             messages.error(request,"authentication is failed")
#             return redirect("login")
#         return render(request,"account/login.html")