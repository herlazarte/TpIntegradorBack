# Generated by Django 5.1 on 2024-11-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contra', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('localidad', models.CharField(default='', max_length=255)),
                ('provincia', models.CharField(default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
