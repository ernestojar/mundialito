# Generated by Django 4.2.11 on 2024-04-01 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0006_alter_calendario_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendario',
            name='partido',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.partido', verbose_name='Partido'),
        ),
    ]
