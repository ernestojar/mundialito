# Generated by Django 4.2.11 on 2024-04-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_equipo_resultado_ganador'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='puntos',
            field=models.IntegerField(default='0', verbose_name='Puntos'),
        ),
    ]
