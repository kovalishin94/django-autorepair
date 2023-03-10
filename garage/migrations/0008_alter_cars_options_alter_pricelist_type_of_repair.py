# Generated by Django 4.1.6 on 2023-02-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0007_alter_manufacturers_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'ordering': ['date_of_application'], 'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='type_of_repair',
            field=models.CharField(max_length=150, unique=True, verbose_name='Вид ремонтных работ'),
        ),
    ]
