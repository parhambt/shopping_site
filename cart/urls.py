from django.urls import path
from .views import cart_view ,add_cart ,miness_cart ,remove_cart, check_out
urlpatterns = [path("",cart_view,name="cart_view"),
               path("add_cart/<int:product_id>/",add_cart , name='add_cart'),
               path('miness_cart/<int:product_id>',miness_cart,name='miness_cart'),
               path('remove_cart/<int:product_id>/<str:variation>/',remove_cart,name='remove_cart'),
               path("checkout/",check_out,name="checkout"),

               

] 