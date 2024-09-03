# Generated by Django 4.2.11 on 2024-04-01 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0007_alter_calendario_partido'),
    ]

    operations = [
        migrations.CreateModel(
            name='equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.CharField(max_length=100, verbose_name='Equipo')),
            ],
        ),
        migrations.AddField(
            model_name='resultado',
            name='ganador',
            field=models.CharField(default='Empate', max_length=100, verbose_name='Ganador'),
        ),
    ]
