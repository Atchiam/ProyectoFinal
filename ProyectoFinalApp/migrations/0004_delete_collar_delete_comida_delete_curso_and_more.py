# Generated by Django 4.0.5 on 2022-07-22 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoFinalApp', '0003_alter_blogcard_fecha'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Collar',
        ),
        migrations.DeleteModel(
            name='Comida',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Evento',
        ),
        migrations.DeleteModel(
            name='Pipeta',
        ),
    ]
