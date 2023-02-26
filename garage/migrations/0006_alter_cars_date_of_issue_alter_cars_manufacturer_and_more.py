# Generated by Django 4.1.6 on 2023-02-11 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0005_pricelist_alter_cars_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='date_of_issue',
            field=models.DateField(verbose_name='Дата окончания ремонта'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='garage.manufacturers', verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.owners', verbose_name='Владелец'),
        ),
    ]
