from django.urls import path
from .views import add_pet, get_pet, get_pets, get_pets_by_type, change_pet, buy_pet

urlpatterns = [
    path('add_pet', add_pet),                       # Добавить                          POST
    path('get_pet_by_id', get_pet),                       # Получить инфу о животном          GET
    path('get_pets', get_pets),                     # Вывести инфу о всех животных      GET
    path('get_pets_by_type', get_pets_by_type),     # Вывести инфу по типу              GET
    path('buy_pet', buy_pet),                       # Купить                            DELETE
    path('change_pet', change_pet)                  # Изменить любую инфу о животном    POST
]