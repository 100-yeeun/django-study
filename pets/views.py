import json
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PetSerializer
from .models import Pet
from django.views import View
from django.http import HttpResponse, JsonResponse
# Create your views here.

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

