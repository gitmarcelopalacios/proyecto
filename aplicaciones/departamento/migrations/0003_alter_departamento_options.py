# Generated by Django 4.0.3 on 2022-04-09 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_remove_departamento_nombre_departamento_anulate_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-id'], 'verbose_name': 'Depto', 'verbose_name_plural': 'Áreas de la empresa'},
        ),
    ]