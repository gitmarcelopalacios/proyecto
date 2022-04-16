# Generated by Django 4.0.3 on 2022-04-13 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tipo_documento', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='dni',
        ),
        migrations.AddField(
            model_name='cliente',
            name='numdocumento',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipodocumento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tipo_documento.tipo_documento'),
        ),
    ]
