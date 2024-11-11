# Generated by Django 5.1 on 2024-11-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0004_alter_solicitud_tipo_servicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='estado_turno',
            field=models.CharField(choices=[('A', 'Aceptado'), ('EN', 'En transcurso'), ('R', 'Rechazado')], max_length=3),
        ),
    ]