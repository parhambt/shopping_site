from django.shortcuts import render , redirect ,get_object_or_404
from store.models import Product 
from .models import Cart , CartItem
from django.contrib.auth.decorators import login_required
import json
# Create your views here.
def cart_id(request):
    cart_session=request.session.session_key
    if not cart_session : 
        cart_session=request.session.create()
    return cart_session


def add_cart(request,product_id):
    curent_user=request.user

    color=request.POST.get('color')
    size=request.POST.get('size')
    sample={'color':color , "size":size}
    
    product=Product.objects.get(id=product_id)
    if curent_user.is_authenticated  :

        try : 
            
            cart_item=CartItem.objects.get(product=product,user=curent_user,json_variation=sample , cart=None)
            
            cart_item.quantity +=1
            
            
        except CartItem.DoesNotExist : 
            cart_item=CartItem.objects.create(product=product,user=curent_user,quantity=1,json_variation=sample)
            
        # cart_item.json_variation=all_query_list
        # in_cart_already=CartItem.objects.filter(product=product,cart__cart_id=cart_id(request))

        cart_item.save()
        # print(product.id)
        
        return redirect('cart_view')
    else :

        try : 
            cart=Cart.objects.get(cart_id=cart_id(request))
        except Cart.DoesNotExist  :
            cart=Cart.objects.create(cart_id=cart_id(request))
        cart.save()
        try : 
            
            cart_item=CartItem.objects.get(product=product,cart=cart,json_variation=sample)
            cart_item.quantity +=1
            
        except CartItem.DoesNotExist : 
            cart_item=CartItem.objects.create(product=product,cart=cart,quantity=1,json_variation=sample)
        # cart_item.json_variation=all_query_list
        in_cart_already=CartItem.objects.filter(product=product,cart__cart_id=cart_id(request))

        cart_item.save()
        # print(product.id)
        
        return redirect('cart_view')

def miness_cart(request,product_id):
    curent_user=request.user
    color=request.POST.get('color')
    size=request.POST.get('size')
    sample={'color':color , "size":size}
    product=get_object_or_404(Product,id=product_id)
    if curent_user.is_authenticated : 
        cart_item=CartItem.objects.get(user=curent_user,product=product,json_variation=sample)
        if cart_item.quantity > 1 : 
            cart_item.quantity -=1
            cart_item.save()
        else : 
            cart_item.delete()
        return redirect("cart_view")

        pass
    else : 

        cart=get_object_or_404(Cart,cart_id=cart_id(request))
        cart_item=CartItem.objects.get(cart=cart,product=product,json_variation=sample)
        if cart_item.quantity > 1 : 
            cart_item.quantity -=1
            cart_item.save()
        else : 
            cart_item.delete()


        return redirect('cart_view')

def remove_cart(request,product_id,variation) : 
    variation= variation.replace("'", "\"")
    variation=json.loads(variation)

    curent_user=request.user
    product=get_object_or_404(Product,id=product_id)
    if curent_user.is_authenticated : 
        cart_item=CartItem.objects.get(user=curent_user,product=product,json_variation=variation)
        cart_item.delete()
        return redirect('cart_view')
        pass
    else : 
    
        cart=get_object_or_404(Cart,cart_id=cart_id(request))
        cart_item=CartItem.objects.get(cart=cart,product=product,json_variation=variation)
        cart_item.delete()
        return redirect('cart_view')



def cart_view(request,cart_items=None,quantity=0,total=0):
    try : 
        
        if request.user.is_authenticated : 
            cart_items=CartItem.objects.filter(user=request.user)
            
        else : 
            cart=Cart.objects.get(cart_id=cart_id(request))
        
            cart_items=CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items : 
            
            quantity += cart_item.quantity
            total += cart_item.product.price * cart_item.quantity
    except : 
        pass
    
    context={'quantity':quantity,"total":total,"cart_items":cart_items,"total_with_tax":total+10}


    return render(request,"cart/cart.html",context)

@login_required(login_url="login")
def check_out(request,cart_items=None,quantity=0,total=0):
    curent_user=request.user
    try : 
        
        
        cart_items=CartItem.objects.filter(user=curent_user,is_active=True)
        for cart_item in cart_items : 
            
            quantity += cart_item.quantity
            total += cart_item.product.price * cart_item.quantity
    except : 
        pass
    
    context={'quantity':quantity,"total":total,"cart_items":cart_items,"total_with_tax":total+10}
    return render(request,"cart/checkout.html",context)

