# Generated by Django 4.1.6 on 2023-02-06 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Модель')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Производитель')),
            ],
        ),
        migrations.CreateModel(
            name='Mechanics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=150, verbose_name='Отчество')),
                ('experience', models.IntegerField(verbose_name='Опыт работы')),
            ],
        ),
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=150, verbose_name='Отчество')),
                ('first_application', models.DateTimeField(auto_now_add=True, verbose_name='Дата первого обращения')),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=150, verbose_name='Цвет автомобиля')),
                ('type_of_repair', models.CharField(max_length=150, verbose_name='Вид ремонтных работ')),
                ('gov_number', models.CharField(max_length=10, verbose_name='Гос. номер')),
                ('ser_sts', models.CharField(max_length=4, verbose_name='Серия СТС')),
                ('num_sts', models.IntegerField(max_length=6, verbose_name='Номер СТС')),
                ('date_of_application', models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')),
                ('date_of_issue', models.DateTimeField(blank=True, verbose_name='Дата окончания ремонта')),
                ('photo', models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Фото')),
                ('scan_sts', models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='Скан ПТС')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='garage.carmodels', verbose_name='Модель')),
                ('manufacturer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='garage.manufacturers', verbose_name='Производитель')),
                ('mechanic', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='garage.mechanics', verbose_name='Механик')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='garage.owners')),
            ],
        ),
        migrations.AddField(
            model_name='carmodels',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='garage.manufacturers'),
        ),
    ]
