# Generated by Django 5.1 on 2024-11-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesional', '0003_profesional_nombredeusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='NombreDeUsuario',
            field=models.CharField(default='', max_length=255),
        ),
    ]
