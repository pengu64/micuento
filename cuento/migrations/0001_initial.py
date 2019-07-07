# Generated by Django 2.2.2 on 2019-07-01 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Apellido_p', models.CharField(max_length=40)),
                ('Apellido_m', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=256)),
                ('Ciudad', models.CharField(max_length=50)),
                ('Alcaldia', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=120)),
                ('CPostal', models.IntegerField(max_length=7)),
                ('Genero', models.CharField(max_length=1)),
                ('Fecha_subscripcion', models.DateField(auto_now_add=True)),
                ('Telefono', models.BigIntegerField(max_length=14)),
            ],
        ),
    ]
