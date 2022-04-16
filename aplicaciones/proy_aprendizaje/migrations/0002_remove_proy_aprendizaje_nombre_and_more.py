# Generated by Django 4.0.3 on 2022-04-13 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('proy_aprendizaje', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proy_aprendizaje',
            name='nombre',
        ),
        migrations.AddField(
            model_name='proy_aprendizaje',
            name='departamento',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
    ]
