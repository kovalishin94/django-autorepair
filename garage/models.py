from django.db import models
from django.urls import reverse


class Cars(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturers', 
        on_delete=models.PROTECT, 
        verbose_name='Производитель',
        )
    car_model = models.ForeignKey('CarModels', on_delete=models.PROTECT, verbose_name='Модель')
    color = models.CharField(max_length=150, verbose_name='Цвет автомобиля')
    owner = models.ForeignKey('Owners', on_delete=models.CASCADE, verbose_name='Владелец')
    type_of_repair = models.ManyToManyField('PriceList', verbose_name='Вид ремонтных работ')
    gov_number = models.CharField(max_length=10, verbose_name='Гос. номер')
    year = models.IntegerField(verbose_name='Год выпуска')
    ser_sts = models.CharField(max_length=4, verbose_name='Серия СТС')
    num_sts = models.IntegerField(verbose_name='Номер СТС')
    date_of_application = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')
    date_of_issue = models.DateField(verbose_name='Дата окончания ремонта')
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Фото')
    scan_sts = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='Скан ПТС')
    mechanic = models.ForeignKey('Mechanics', on_delete=models.PROTECT, verbose_name='Механик', blank=True)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['-date_of_issue']
    
    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})
    

class Owners(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    second_name = models.CharField(max_length=150, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=150, verbose_name='Отчество', blank=True)
    first_application = models.DateTimeField(auto_now_add=True, verbose_name='Дата первого обращения', editable=False)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
    
    def __str__(self):
        return self.second_name


class Manufacturers(models.Model):
    title = models.CharField(max_length=150, verbose_name='Производитель', unique=True)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = ['title']

    def __str__(self):
        return self.title


class CarModels(models.Model):
    title = models.CharField(max_length=150, verbose_name='Модель')
    manufacturer = models.ForeignKey('Manufacturers', on_delete=models.PROTECT, verbose_name='Производитель', related_name='carmod')
    
    def __str__(self):
        return self.title    

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Mechanics(models.Model):
    second_name = models.CharField(max_length=150, verbose_name='Фамилия')
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    patronymic = models.CharField(max_length=150, verbose_name='Отчество', blank=True)
    experience = models.IntegerField(verbose_name='Опыт работы')

    class Meta:
        verbose_name = 'Механик'
        verbose_name_plural = 'Механики'

    def __str__(self):
        return self.second_name
    

class PriceList(models.Model):
    type_of_repair = models.CharField(max_length=150, verbose_name='Вид ремонтных работ', unique=True)
    price = models.IntegerField(verbose_name='Стоимость работы')

    class Meta:
        verbose_name = 'Прайс-лист'
        verbose_name_plural = 'Прайс-лист'  

    def __str__(self):
        return self.type_of_repair
    
    def get_absolute_url(self):
        return reverse("price_detail", kwargs={"pk": self.pk})
    
    
    