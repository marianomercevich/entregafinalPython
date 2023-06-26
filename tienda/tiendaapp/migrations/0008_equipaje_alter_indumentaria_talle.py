# Generated by Django 4.0.5 on 2022-07-16 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaapp', '0007_remove_accesorio_talle_alter_indumentaria_talle'),
    ]

    operations = [
        migrations.CreateModel(
            name='equipaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca')),
                ('tipo', models.CharField(max_length=30, verbose_name='Tipo')),
                ('precio', models.FloatField(verbose_name='Precio $')),
            ],
        ),
        migrations.AlterField(
            model_name='indumentaria',
            name='talle',
            field=models.CharField(max_length=30, verbose_name='Talle'),
        ),
    ]
