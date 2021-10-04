from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Products
from .serializers import ProductSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny

# Create your views here.

class ProductsCRUD(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAdminUser]