import json
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from django.views import View
from django.http import HttpResponse, JsonResponse
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
