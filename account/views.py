from django.shortcuts import render ,redirect
from django.http import HttpResponse 
from .forms import RegisterationForm
from django.views import View
from . models import CustomeUser
from django.contrib import messages , auth 
# verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator  
from  django.core.mail import EmailMessage ,send_mail


def resend_verification(request):
    pass

class Register(View):
    def send_verification(self,request,user) :
         
        pass
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
            
            current_site=get_current_site(request)
            mail_subject="Please activate your account"
            mail_content=render_to_string("account/account_verification.html",{"user":user,
            'domain':current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            "token":default_token_generator.make_token(user),

            
            })
            to_email=email
            send_email=EmailMessage(mail_subject,mail_content, to=[to_email])
            send_email.send()
            user.save()
            messages.success(request,"Registration is success \n Please verify your Gmail")
            
            return redirect('register')
        elif form.has_error(email) and user.is_active==False : 



        else : 
            print(form.errors.as_json)
            
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


def activate(request,uidb64,token):
    try : 
        uid = urlsafe_base64_decode( uidb64).decode()
        user=CustomeUser._default_manager.get(pk=uid)
        print("here is user")
        print(user)
    except :
        print("Failure")
        user=None
    if user is not None and default_token_generator.check_token(user,token) :
        user.is_active=True
        user.save() 
        messages.success(request, "Cangrats your account is activated")
        return redirect("login")
    else : 
        messages.error(request,"invalid activation link")
        return redirect("register")
    

    return HttpResponse("Ok")
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