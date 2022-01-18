from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializer import FruitSerializer
from .models import Fruit

class FruitViewsets(ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    permission_classes = [permissions.AllowAny]