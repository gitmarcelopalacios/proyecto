# Generated by Django 4.0.3 on 2022-04-15 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detalle_cuenta', '0002_detalle_cuenta_idasiento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalle_cuenta',
            old_name='detalle',
            new_name='referencia',
        ),
    ]