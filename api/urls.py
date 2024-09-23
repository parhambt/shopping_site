from django.urls import path 
from . import views
urlpatterns=[path('products/',views.ListProductApi.as_view(), name="product_api_view"),
             

]