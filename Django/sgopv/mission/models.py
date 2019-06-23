from django.db import models
from account.models import Pilot, Instructor
from django.utils.timezone import now


class Fuel(models.Model):
    FUEL_TYPE = (
        ('S', 'Super'),
        ('E', 'Extra'),
        ('D', 'Diesel'),
    )
    brand = models.CharField(verbose_name="Marca", max_length=30)
    type = models.CharField(verbose_name="Tipo", max_length=30, choices=FUEL_TYPE)
    quantity = models.FloatField(verbose_name="Cantidad")

    class Meta:
        verbose_name = "Combustible"
        verbose_name_plural = "Combustibles"

    def __str__(self):
        return self.brand


class Route(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=300)
    coordinates = models.CharField(verbose_name="Coordenadas", max_length=300)
    description = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural = "Rutas"

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=30)
    quantity = models.IntegerField(verbose_name="Cantidad")
    detaill = models.TextField(verbose_name="Detalle")
    material = models.CharField(verbose_name="Material", max_length=30)

    class Meta:
        verbose_name = 'Equipamiento'
        verbose_name_plural = 'Equipamiento'

    def __str__(self):
        return self.name


class Origin(models.Model):
    place = models.CharField(verbose_name="Origen", max_length=100)
    time = models.TimeField(verbose_name="Hora")
    description = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Origen"
        verbose_name_plural = "Origenes"

    def __str__(self):
        return self.place


class Destination(models.Model):
    place = models.CharField(verbose_name="Destino", max_length=100)
    time = models.TimeField(verbose_name="Hora")
    description = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"

    def __str__(self):
        return self.place


class FlyMission(models.Model):
    pilot = models.ForeignKey(Pilot, verbose_name="Piloto", related_name="missions_pilot", on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, verbose_name="Instructor", related_name="missions_instructor",
                                   on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, verbose_name="Gasolina", on_delete=models.DO_NOTHING, null=True)
    equipment = models.ManyToManyField(Equipment, verbose_name="Equipamiento", related_name="missions_equipment")
    routes = models.ManyToManyField(Route, verbose_name="Rutas", related_name="missions_route")
    origin = models.ForeignKey(Origin, verbose_name="Origen",
                               related_name="missions_origin", on_delete=models.DO_NOTHING, null=True)
    destination = models.ForeignKey(Destination, verbose_name="Destino",
                                    related_name="missions_destination", on_delete=models.DO_NOTHING, null=True)
    distance = models.FloatField(verbose_name="Distancia")
    time = models.TimeField(verbose_name="Tiempo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Mision de Vuelo"
        verbose_name_plural = "Misiones de Vuelo"

    def __str__(self):
        return self.pilot.user.first_name + " " + self.pilot.user.last_name


class Plane(models.Model):
    plate = models.CharField(verbose_name="Placa", max_length=10)
    model = models.CharField(verbose_name="Modelo", max_length=100)
    brand = models.CharField(verbose_name="Marca", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Avión"
        verbose_name_plural = "Aviones"

    def __str__(self):
        return self.model + "-" + self.brand


class Planning(models.Model):
    mission = models.ForeignKey(FlyMission, verbose_name="Misión",
                                related_name="planning_mission", on_delete=models.CASCADE)
    plane = models.ForeignKey(Plane, verbose_name="Avión", related_name="planning_plane", on_delete=models.DO_NOTHING)
    date = models.DateTimeField(verbose_name="Fecha", default=now)
    objective = models.TextField(verbose_name="Objetivo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Planificación"
        verbose_name_plural = "Planificaciones"

    def __str__(self):
        return "{} {} - {}".format(self.mission.pilot.user.first_name,
                                   self.mission.pilot.user.last_name, self.plane.model)
