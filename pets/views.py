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

class UpdateAge(View):
    def put(self, request, pet_id):
        print('ddd')
        try:
            if Pet.objects.filter(id=pet_id).exists():
                data = json.loads(request.body)
                Pet.objects.filter(id=pet_id).update(
                    name = data['name'],
                    species = date['species'],
                    age = data['age'],
                )

                return HttpResponse(status=200)

            return JsonResponse({'massage':'INVALID_PET'},status=401)

        except KeyError:
            return JsonResponse({'massage':'INVALID_KEYS'}, status=400)
