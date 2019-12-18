from rest_framework import serializers
from .models import Pet


"""
    todo
    POST + json Добавить животное (Имя, цена, тип) => id
    POST/UPDATE + id + json Изменить цену
    DELETE + id Купить животное
    GET + id Вывести инфу о животном
    GET + type Вывести всех животных по типу
    GET Вывести вообще всех животных
"""


class NewPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('name', 'price', 'pet_type')


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'price', 'pet_type')


class PetPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'price')
