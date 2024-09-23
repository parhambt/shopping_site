
from django.urls import path
from .views import store_view , info_product,Search

# app_name='store'
urlpatterns = [ path("",store_view ,name="store_view"),
              path("category/<slug:slug_category>/",store_view,name="product_by_category") ,
              path("category/<slug:slug_category>/<slug:info_product_slug>/",info_product,name="info_product"),
              path("search/",Search.as_view() , name='search')

] 