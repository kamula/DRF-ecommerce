from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Category
from .serializers import CategorySerializer

@extend_schema(responses=CategorySerializer)
class CategoryViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all categories
    """

    queryset = Category.objects.all()


    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
