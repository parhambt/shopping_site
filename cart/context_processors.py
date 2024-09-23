from .views import cart_id
from .models import Cart , CartItem
def count_cart_items(request):
    number= 0
    if "admin" in request.path : 
        return {}
    else : 
        try : 
            cart=Cart.objects.get(cart_id=cart_id(request))
           
            cart_items=CartItem.objects.filter(cart=cart)
            
            for cart_item in cart_items : 
                number += cart_item.quantity
        except  :
            number=0
        return ( {"count_itmes":number})