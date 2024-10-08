from django.shortcuts import render ,redirect
from cart.models import CartItem
from .forms import OrderForm
from .models import Order , OrderProduct
import datetime
# Create your views here.
def place_order(request):
    curent_user=request.user
    cart_items=CartItem.objects.filter(user=curent_user)
    if cart_items.count() <= 0 : 
        return redirect("store_view")
    
    total_price=0
    tax=0
    for cart_item in cart_items  :
        total_price += (cart_item.product.price * cart_item.quantity)
    tax=(2*total_price)/100
    grand_total = tax + total_price

    
    if request.method == "POST":

        form=OrderForm(request.POST)
        if form.is_valid():
            
            data=form.save(commit=False)

            
            data.user=curent_user
            
            data.order_total=grand_total
            data.tax=tax
            data.ip=request.META.get("REMOTE_ADDR")
            #create pk(id)
            yr=int(datetime.date.today().strftime("%Y"))
            dt=int(datetime.date.today().strftime("%d"))
            mt=int(datetime.date.today().strftime("%m"))
            d=datetime.date(yr,mt,dt)
            curent_date=d.strftime("%Y%m%d")
            order_number=curent_date + str(data.id)
            data.order_number=order_number
            data.save()
            order=Order.objects.get(user=curent_user , is_orderd=False , order_number=order_number)
            context={
                "order":order,
                "total_price":total_price,
                "grand_total":grand_total,
                "tax":tax,
                "cart_items":cart_items
            }
            return render(request,"orders/payments.html",context)
    else : 
        return redirect("checkout")

def payment(request):
    
    return render(request,"orders/payments.html")







        
        
        

    




