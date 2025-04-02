from django.shortcuts import render_to_response
from rest_framework import generics, permissions, filters # type: ignore
from .models import User, Product, Category
from .serializers import UserSerializer, ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from rest_framework.exceptions import NotFound # type: ignore
from rest_framework.exceptions import PermissionDenied # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore




# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [permissions.AllowAny] # Anyone can register

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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

    def get_object(self):
        """ Handle 404 if product is not found """
        try:
            return super().get_object()
        except Product.DoesNotExist:
            raise NotFound({"error": "Product not found."})
        
    def update(self, request, *args, **kwargs):
        """ Ensure only authenticated users can update """
        if not request.user.is_authenticated:
            raise PermissionDenied({"error": "You must be authenticaed in to update a product."})

        return super().update(request, *args, **kwargs)



class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permissions_classes = [permissions.IsAdminUser] # Only Admins can create new categories

    def create(self, request, *args, **kwargs):
        """ Only admins can create categories """
        if not request.user.is_staff:
            return Response({"error": "Only admins can create categories."}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permissions_classes = [permissions.IsAdminUser] #Only Admins can modify

    def get_object(self):
        """ Handle 404 if product is not found """
        try:
            return super().get_object()
        except Product.DoesNotExist:
            raise NotFound({"error": "Product not found."})

