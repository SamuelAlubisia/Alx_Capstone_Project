from django.urls import path
from .views import ProductDetailView, ProductListCreateView, UserListCreateView, UserDetailView, CategoryDetailView, CategoryListCreateView, RegisterView, LoginView, LogoutView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name= 'user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListCreateView.as_view(), name= 'product-list-create'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    # Authentication routes
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]