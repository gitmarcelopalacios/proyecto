# Generated by Django 4.0.3 on 2022-04-16 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyecto_tarea', '0001_initial'),
        ('estado_tarea', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha:')),
                ('detalle', models.CharField(max_length=200, verbose_name='Detalle:')),
                ('observaciones', models.CharField(default='', max_length=20, verbose_name='Observaciones:')),
                ('id_estado_tarea', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='estado_tarea.estado_tarea')),
                ('id_proyecto_tarea', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proyecto_tarea.proyecto_tarea')),
            ],
        ),
    ]
