# Generated by Django 4.0.6 on 2022-07-15 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_alter_prospecto_fechareg'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospecto',
            name='coordenadas',
            field=models.CharField(max_length=100, null=True, verbose_name='Coordenadas'),
        ),
        migrations.AlterField(
            model_name='prospecto',
            name='localidad',
            field=models.CharField(max_length=200, verbose_name='Localidad'),
        ),
    ]