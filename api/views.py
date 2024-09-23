from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Product
from .serializers import ProductSerializer
from rest_framework import generics
# Create your views here.
class ListProductApi(generics.ListAPIView) : 
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


    