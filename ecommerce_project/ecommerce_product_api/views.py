from django.shortcuts import render
from rest_framework import viewsets, permissions # type: ignore
from .models import User, Product, Category
from .serializers import UserSerializer, ProductSerializer, CategorySerializer

#Create your views here