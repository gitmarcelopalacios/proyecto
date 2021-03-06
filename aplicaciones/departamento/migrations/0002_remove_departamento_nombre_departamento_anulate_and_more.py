# Generated by Django 4.0.3 on 2022-04-08 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='nombre',
        ),
        migrations.AddField(
            model_name='departamento',
            name='anulate',
            field=models.BooleanField(default=False, verbose_name='Anulado'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='name',
            field=models.CharField(default=' ', max_length=50, verbose_name='Nombre:'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='shor_name',
            field=models.CharField(default=' ', max_length=20, verbose_name='Nombre Corto:'),
        ),
    ]
