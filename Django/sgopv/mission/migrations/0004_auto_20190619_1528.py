# Generated by Django 2.2.2 on 2019-06-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0003_auto_20190619_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='flymission',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='mission.Categories', verbose_name='Categorias'),
        ),
    ]
