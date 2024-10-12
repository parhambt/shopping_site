from django.shortcuts import render
from store.models import Product ,ReviewRaiting
def home_view(request):

    products=Product.objects.all().filter(is_availeble=True).order_by("-created_date")
    for product in products : 
        reviews=ReviewRaiting.objects.filter(product=product,status=True)

    context={'products':products}

    return render(request,"index.html",context)