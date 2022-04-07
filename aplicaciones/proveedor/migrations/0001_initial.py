# Generated by Django 4.0.3 on 2022-04-06 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido(s):')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre(s):')),
                ('email', models.EmailField(max_length=200, verbose_name='Email:')),
                ('domicilio', models.CharField(max_length=100, verbose_name='Domicilio:')),
                ('dni', models.CharField(max_length=20, verbose_name='DNI:')),
                ('cuilcuit', models.CharField(max_length=20, verbose_name='CUIL O CUIT:')),
            ],
        ),
    ]