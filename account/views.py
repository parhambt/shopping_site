from django.shortcuts import render ,redirect , get_object_or_404
from django.http import HttpResponse 
from .forms import RegisterationForm ,UserForm, ProfileForm
from django.views import View
from . models import CustomeUser ,UserProfile
from django.contrib import messages , auth 
from django.contrib.auth.decorators import login_required
from cart.views import cart_id
from cart.models import Cart , CartItem
import requests
# verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator  
from  django.core.mail import EmailMessage ,send_mail
from django.conf import settings




class Register(View):
    def resend_verification(self,request,user) :
        pass
    def send_verification(self,request,user) :
        token=default_token_generator.make_token(user)
        
        uid=urlsafe_base64_encode(force_bytes(user.pk))
        current_site=get_current_site(request)
        mail_subject="Please activate your account"
        print(f"token is {token}")
        mail_content=render_to_string("account/account_verification.html",{"user":user,
        'domain':current_site,
        'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
        "token":token,

        
        })
        
        send_mail(
        mail_subject,
        mail_content,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
        

    def post(self,request):
        email_error=True
        form=RegisterationForm(request.POST)
        form_json=form.errors.as_json()
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
            self.send_verification(request,user)
            user.save()
            

            
            
            return redirect(f'/account/login/?command=verification&email={email}')




        
        else : 
            
            print(form.errors.as_json)
            context={'form':form,"email_error":email_error}
        
            
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
            try : # bring cart items to the real cart
                cart=Cart.objects.get(cart_id=cart_id(request))
                is_cart_items=CartItem.objects.filter(cart=cart).exists()
                if is_cart_items : 
                    cart_items=CartItem.objects.filter(cart=cart)
                    for cart_item in cart_items : 
                        filter_item=CartItem.objects.filter(user=user,product=cart_item.product,json_variation=cart_item.json_variation).exists()
                        if filter_item : 
                            cart_item_quantity=cart_item.quantity
                            item=CartItem.objects.get(user=user,product=cart_item.product)
                            item.quantity += cart_item_quantity
                            item.save()
                        else : 
                            cart_item.user=user
                            cart_item.cart = None 
                            cart_item.save()


            except : 
                pass

            auth.login(request=request,user=user)
            
            messages.success(request,"authentication is succseed")
            url=request.META.get("HTTP_REFERER")
            try : 
                query=requests.utils.urlparse(url).query
                params=dict(x.split("=") for x in query.split('&'))
                if "next" in params : 
                    next_page=params.get('next')
                    print(next_page)
                    return redirect(next_page)
            except :
            
                return redirect("dashboard")
        else : 
            messages.error(request,"Error : authentication is failed")
            return redirect("login")
    
    elif request.method == "GET" : 
        
        return render(request,"account/login.html")


@login_required(login_url="login")      
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
        user=CustomeUser.objects.get(pk=uid)
        print("here is token in activation")
        print(token)
        print("here is uidb64")
        print(uidb64)
        
        print(default_token_generator.check_token(user,token))
    except :
        print("Failure")
        user=None
    
    if user is not None  :
        user.is_active=True
        user.save() 
        messages.success(request, "Cangrats your account is activated")
        
        return redirect("login")
    else : 
        messages.error(request,"invalid activation link")
        return redirect("register")
    

    return HttpResponse("Ok")
    pass


@login_required(login_url="login")   
def dashboard(request):
    user_profile=UserProfile.objects.get(user=request.user)
    try : 
        image = user_profile.profile_picture
        context={"user_profile":user_profile,"image":image}
    except:
        image=False
        context={"user_profile":user_profile,"image":image}
    return render(request,"account/dashboard.html",context)


def reset_password_email(request,user) :
    token=default_token_generator.make_token(user)
    
    uid=urlsafe_base64_encode(force_bytes(user.pk))
    current_site=get_current_site(request)
    mail_subject="Please activate your account"
    print(f"token is {token}")
    mail_content=render_to_string("account/reset_password_email.html",{"user":user,
    'domain':current_site,
    'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
    "token":token,

    
    })
    
    send_mail(
    mail_subject,
    mail_content,
    settings.DEFAULT_FROM_EMAIL,
    [user.email],
    fail_silently=False,
)
def reset_passwrod_validate(request,uidb64,token):
    try : 
        uid = urlsafe_base64_decode( uidb64).decode()
        user=CustomeUser.objects.get(pk=uid)
        print("here is token in activation")
        print(token)
        print("here is uidb64")
        print(uidb64)
        
        print(default_token_generator.check_token(user,token))
    except :
        print("Failure")
        user=None
    if user is not None : # token checking is not here make it right later
        request.session["uid"]=uid
        messages.success(request,"Please reset your password")
        return redirect("resetpassword")

    else : 
        messages.error(request,"this link is expiered")
        return redirect("login")

        

def forget_pass(request):
    if request.method=="POST" :
        email=request.POST.get("email")
        if CustomeUser.objects.filter(email=email).exists() : 
            user=CustomeUser.objects.get(email__exact=email)
            reset_password_email(request,user)
            messages.success(request,"your password is successfully reset")
            return redirect("login")
            


        else : 
            messages.error(request,"this email does not exists")
    return render(request,"account/forgot_password.html")
   
class ResetPassword(View):
    def post(self,request):
        password=request.POST.get("password")
        confirm_pass=request.POST.get("confirm_password")
        if password == confirm_pass  :
            uid=request.session.get("uid")
            user=CustomeUser.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,"password reset succsefully")
            return redirect("login")
            
        else : 
            messages.error(request,"password does not match please do it more carfully")
            return redirect("resetpassword")

    def get(self,request):
        return render(request,"account/reset_password.html")
@login_required(login_url="login")
def edit_profile(request):
    user_profile = get_object_or_404(UserProfile , user=request.user)
    if request.method == "POST" : 
        user_form=UserForm(request.POST,instance=request.user)
        profile_form=ProfileForm(request.POST , request.FILES , instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid() : 
            user_form.save()
            profile_form.save()
            messages.success(request, "you profile has been updated")
            return redirect("edit_profile")
    else : 
        user_form=UserForm(instance=request.user)
        profile_form=ProfileForm(instance=user_profile)
    status=False
    try :
        x=user_profile.profile_picture.url
        status=True
    except : 
        status=False
    context={"user_form":user_form,"profile_form":profile_form,"user_profile":user_profile,"status":status }


    return render(request,"account/edit_profile.html",context)
    pass
@login_required(login_url="login")
def change_password(request):
    if request.method == "POST":
        curent_pass=request.POST.get("curent_password")
        new_pass=request.POST.get("new_password")
        confirm_pass=request.POST.get("new_password_1")
        user=CustomeUser.objects.get(username__exact=request.user.username)
        if new_pass== confirm_pass : 
            is_success=user.check_password(curent_pass)
            if is_success : 
                user.set_password(new_pass)
                user.save()
                messages.success(request, "Password updated successfully")
                auth.logout(request)
                return redirect("login")
            else : 
                messages.error(request ,"password is not correct")
                return redirect("change_password")
        else : 
            messages.error(request ,"passwords does not match")
            return redirect("change_password")
    else : 


        return render(request , "account/change_password.html")
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