from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from shop_rest_api.models import Pet
from .serializers import NewPetSerializer, PetSerializer


@api_view(['POST'])
def add_pet(request):
    try:
        serializer = NewPetSerializer(data=request.data)
        record = Pet(name=serializer.initial_data['name'], price=serializer.initial_data['price'], pet_type=serializer.initial_data['pet_type'])
        record.save()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def change_pet(request):
    try:
        serializer = PetSerializer(request.data)
        record = Pet.objects.get(id=serializer.data['id'])
        if record.pet_type != serializer.data['pet_type']:
            return Response("can't change pet_type", status=status.HTTP_400_BAD_REQUEST)
        if serializer.data['name'] != "":
            record.name = serializer.data['name']
        if serializer.data['price'] != "":
            record.price = serializer.data['price']
        record.save()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_pet(request):
    try:
        id = request.GET.get('id')
        record = Pet.objects.get(id=id)
        serializer = PetSerializer(record)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def get_pets(request):
    records = Pet.objects.all()
    serializer = PetSerializer(records, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_pets_by_type(request):
    try:
        pet_type = request.GET.get('pet_type')
        records = Pet.objects.filter(pet_type=pet_type)
        serializer = PetSerializer(records, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except:
        return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def buy_pet(request):
    try:
        id = request.GET.get('id')
        record = Pet.objects.get(id=id)
        record.delete()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

