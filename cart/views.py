from django.shortcuts import render , redirect ,get_object_or_404
from store.models import Product 
from .models import Cart , CartItem
# Create your views here.
def cart_id(request):
    cart_session=request.session.session_key
    if not cart_session : 
        cart_session=request.session.create()
    return cart_session


def add_cart(request,product_id):
    
    color=request.POST.get('color')
    size=request.POST.get('size')
    sample={'color':color , "size":size}
    
    product=Product.objects.get(id=product_id)
   
    

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
    color=request.POST.get('color')
    size=request.POST.get('size')
    sample={'color':color , "size":size}
    product=get_object_or_404(Product,id=product_id)
    cart=get_object_or_404(Cart,cart_id=cart_id(request))
    cart_item=CartItem.objects.get(cart=cart,product=product,json_variation=sample)
    if cart_item.quantity > 1 : 
         cart_item.quantity -=1
         cart_item.save()
    else : 
        cart_item.delete()


    return redirect('cart_view')

def remove_cart(request,product_id) : 
    product=get_object_or_404(Product,id=product_id)
    cart=get_object_or_404(Cart,cart_id=cart_id(request))
    cart_item=CartItem.objects.get(cart=cart,product=product)
    cart_item.delete()
    return redirect('cart_view')



def cart_view(request,cart_items=None,quantity=0,total=0):
    try : 
        cart=Cart.objects.get(cart_id=cart_id(request))
        
        cart_items=CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items : 
            
            quantity += cart_item.quantity
            total += cart_item.product.price * cart_item.quantity
    except : 
        pass
    
    context={'quantity':quantity,"total":total,"cart_items":cart_items,"total_with_tax":total+10}


    return render(request,"cart/cart.html",context)



