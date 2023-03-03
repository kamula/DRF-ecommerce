from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


@extend_schema(responses=CategorySerializer)
class CategoryViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all categories
    """

    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


@extend_schema(responses=BrandSerializer)
class BrandViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all brands
    """

    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
