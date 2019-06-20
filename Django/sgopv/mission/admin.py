from django.contrib import admin
from .models import FlyMission, Fuel, Equipment

# En este archivo pueden gestionar los modelos en el panel de administracion
# Al refistrarlos aqui se generan automaticamente los cruds


# Register your models here.
@admin.register(FlyMission)
class FlyMissionAdmin(admin.ModelAdmin):
    pass


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ['brand', 'type'] # Permite mostrar que datos se van a ver en la Lista de Gasolina
    list_filter = ['brand', 'type'] # Son los filtros con los cuales podemos identificar cada uno de los elementos de la lista


