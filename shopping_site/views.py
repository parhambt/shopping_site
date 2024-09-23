from django.shortcuts import render
from store.models import Product
def home_view(request):
    products=Product.objects.all().filter(is_availeble=True)
    context={'products':products}

    return render(request,"index.html",context)