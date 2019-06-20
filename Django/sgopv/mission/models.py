from django.db import models


# Create your models here.
class Fuel(models.Model):
    FUEL_TYPE = (
        ('S', 'Super'),
        ('E', 'Extra'),
        ('D', 'Diesel'),
    )
    brand = models.CharField(verbose_name="Marca", max_length=30)
    type = models.CharField(verbose_name="Tipo", max_length=30, choices=FUEL_TYPE)
    quantity = models.FloatField(verbose_name="Cantidad")

    def __str__(self):
        return self.brand


class Equipment(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=30)
    quantity = models.IntegerField(verbose_name="Cantidad")
    detaill = models.TextField(verbose_name="Detalle")
    material = models.CharField(verbose_name="Material", max_length=30)

    class Meta:
        verbose_name = 'Equipamiento'
        verbose_name_plural = 'Equipamiento'


class FlyMission(models.Model):
    fuel = models.ForeignKey(Fuel, verbose_name="Gasolina", on_delete=models.DO_NOTHING, null=True)
    equipment = models.ManyToManyField(Equipment, verbose_name="Equipamiento", related_name="equipments")
    distance = models.FloatField(verbose_name="Distancia")
    time = models.TimeField(verbose_name="Tiempo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Mision de Vuelo"
        verbose_name_plural = "Misiones de Vuelo"


