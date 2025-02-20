# Generated by Django 5.1.6 on 2025-02-19 12:09

import django.utils.timezone
import landing_page.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('valor_propiedad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(max_length=100)),
                ('creado_en', models.DateTimeField(default=django.utils.timezone.now)),
                ('ubicacion', models.CharField(default=landing_page.models.get_location, max_length=100)),
            ],
        ),
    ]
