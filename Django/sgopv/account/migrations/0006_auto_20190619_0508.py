# Generated by Django 2.2.2 on 2019-06-19 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0005_auto_20190619_0451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.CharField(max_length=10, verbose_name='Cédula')),
                ('profile_type', models.CharField(choices=[('A', 'Administrador'), ('P', 'Piloto'), ('I', 'Instructor'), ('V', 'Visitante')], max_length=2, verbose_name='Tipo de Usuario')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]