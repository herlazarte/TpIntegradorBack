# Generated by Django 5.1 on 2024-11-09 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_direccion_latitud_remove_direccion_longitud_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='profesional',
            name='direccion',
        ),
        migrations.AddField(
            model_name='direccion',
            name='cliente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.cliente'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='profesional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.profesional'),
        ),
    ]