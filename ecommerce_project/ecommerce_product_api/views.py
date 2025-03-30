from django.shortcuts import render
from rest_framework import generics, permissions, filters # type: ignore
from .models import User, Product, Category
from .serializers import UserSerializer, ProductSerializer, CategorySerializer
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend # type: ignore



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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly] # Auth users can create, others can view
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    # Search by name and category (partial match)
    search_fields = ['name', 'category__name']
    
    # Filter by category, price range, and stock availability
    filterset_fields = {
        'category': ['exact'],
        'price': ['gte', 'lte'],  # Price range filtering
        'stock_quantity': ['gte'],  # Only show available stock
    }


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions_classes = [permissions.IsAuthenticated] # Only authenticated users can modify
    lookup_field = 'id'  # Retrieve product by ID

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permissions_classes = [permissions.IsAdmin] # Only Admins can create new categories

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permissions_classes = [permissions.IsAdmin] #Only Admins can modify
