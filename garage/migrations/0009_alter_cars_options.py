# Generated by Django 4.1.6 on 2023-02-19 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0008_alter_cars_options_alter_pricelist_type_of_repair'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'ordering': ['date_of_issue'], 'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
    ]
