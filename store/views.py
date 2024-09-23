from django.shortcuts import render,get_object_or_404 , redirect
from .models import Product
from category.models import Category
from .models import Product
from cart.models import Cart , CartItem
from cart.views import cart_id
from django.core.paginator import Paginator , PageNotAnInteger ,EmptyPage
from django.views import View
# Create your views here.
def store_view(request,slug_category=None , *args ,**kwargs):
    determined_category=None
      
    if slug_category!=None : 
        determined_category=get_object_or_404(Category,slug=slug_category)
        products=Product.objects.all().filter(category=determined_category,is_availeble=True).order_by('id')
        paginator=Paginator(products,6)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)

        products_count=products.count()

     
    else : 
        try : 

            # print(kwargs['search_context']["searched_products"]) 
            products=kwargs['search_context']["searched_products"]
        except : 
            products=Product.objects.all().filter(is_availeble=True).order_by("id")
        paginator=Paginator(products,6)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        products_count=products.count()
        
    context={'products':page_obj,
             "products_count":products_count,
             "pages": range(1,page_obj.paginator.num_pages+1 )
             }
    return render(request,"store/store.html",context)
def info_product(request,info_product_slug,slug_category):
    try : 
        single_product=Product.objects.get(slug=info_product_slug,category__slug=slug_category)
        # product_cartitem=single_product.cartitem_set.get(cart__cart_id=cart_id(request))
        # product_json_variation=product_cartitem.json_variation
        # print('hello')
        # print(product_cartitem)
        # print(product_json_variation)
        is_in_cart_already=CartItem.objects.filter(product=single_product,cart__cart_id=cart_id(request)).exists()
    except Exception as e  :
        raise e 
    context={"single_product":single_product,"is_in_cart_already":is_in_cart_already}
    # for color in single_product.variation.colors.all(): 
    #     print(color)


    return render(request,"store/product_info.html",context)



class Search(View)  :
    def post(self,request) : 
        try : 
            key_word=request.POST.get('keyword')
            products=Product.objects.all().filter(product_name__icontains=key_word , is_availeble=True)
            search_context={"searched_products":products}
            return store_view(request=request,search_context=search_context)
        except : 
            return redirect("store_view")