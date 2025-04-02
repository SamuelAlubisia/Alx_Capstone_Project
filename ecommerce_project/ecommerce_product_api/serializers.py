from rest_framework import serializers # type: ignore
from .models import User, Product, Category
from django.contrib.auth import get_user_model

User = get_user_model() 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Hide password in responses

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  # Hashes password automatically
        )
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'user', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_at']

    def validate_price(self, value):
        """ Ensure price is greater than zero """
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
    
    def validate_stock_quantity(self, value):
        """ Ensure stock is not negative """
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'