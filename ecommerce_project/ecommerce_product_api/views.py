from django.shortcuts import render
from rest_framework import generics, permissions # type: ignore
from .models import User, Product, Category
from .serializers import UserSerializer, ProductSerializer, CategorySerializer
from django.contrib.auth import get_user_model


# Create your views here.
User = get_user_model()

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serialzier_class = UserSerializer
    permissions_classes = [permissions.AllowAny] # Anyone can register

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serialzier_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticated] # Only authenticated users
    
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.object.all()
    serializer_class = ProductSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly] # Auth users can create, others can view

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.object.all()
    serializer_class = ProductSerializer
    permissions_classes = [permissions.IsAuthenticated] # Only authenticated users can modify

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.object.all()
    serializer_class = CategorySerializer
    permissions_classes = [permissions.IsAdmin] # Only Admins can create new categories

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.object.all()
    serializer_class = CategorySerializer
    permissions_classes = [permissions.IsAdmin] #Only Admins can modify
