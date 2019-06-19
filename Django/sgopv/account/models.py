from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # PROFILE_TYPE = (
    #     ('A', 'Administrador'),
    #     ('P', 'Piloto'),
    #     ('I', 'Instructor'),
    #     ('V', 'Visitante'),
    # )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    id_card = models.CharField(max_length=10, verbose_name="Cédula")
    # profile_type = models.CharField(max_length=2, verbose_name="Tipo de Usuario", choices=PROFILE_TYPE)


class Pilot(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    cellphone = models.CharField(verbose_name="Teléfono", max_length=20)

