# Generated by Django 4.0.3 on 2022-04-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=20)),
            ],
        ),
    ]
