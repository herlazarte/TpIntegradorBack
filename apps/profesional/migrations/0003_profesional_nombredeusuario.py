# Generated by Django 5.1 on 2024-11-13 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesional', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesional',
            name='NombreDeUsuario',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
