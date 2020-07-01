from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PetSerializer
from .models import Pet

# Create your views here.

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer