from django.shortcuts import render ,redirect
from cart.models import CartItem
from .forms import OrderForm
# Create your views here.
def place_order(request):
    curent_user=request.user
    cart_items=CartItem.objects.filter(user=curent_user)
    if cart_items.count() <= 0 : 
        return redirect("store_view")
    if request.method == "POST":
        form=OrderForm(request.POST)
        

    pass




