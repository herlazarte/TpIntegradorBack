# Generated by Django 5.1.1 on 2024-10-18 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_servicio', models.CharField(max_length=255)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfesionalServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.profesional')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.servicio')),
            ],
        ),
        migrations.AddField(
            model_name='servicio',
            name='tipo_servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.tiposervicio'),
        ),
    ]
