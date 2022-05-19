from django.db import models
from django_countries.fields import CountryField


class CarType(models.Model):
    car_type = models.CharField(max_length=100, verbose_name="Вид авто")
    title = models.CharField(max_length=150, verbose_name="Название авто")
    year = models.IntegerField(default=0,verbose_name="Год выпуска")
    price = models.FloatField(verbose_name="Цена авто")
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Вид авто'
        verbose_name_plural = 'Виды авто'
        ordering = ['-time_create', 'car_type']


class Salon(models.Model):
    name = models.CharField(max_length=150,verbose_name="Название салона")
    location = CountryField(verbose_name="Местоположение")
    car = models.ManyToManyField(CarType)
    number_of_cars = models.IntegerField(null=True, verbose_name="Количество авто")
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'
        ordering = ['-time_create', 'name']


class Buyer(models.Model):
    name = models.CharField(max_length=150,verbose_name="Имя покупателя")
    balance = models.FloatField(verbose_name="Баланс")
    email = models.EmailField(max_length=254,verbose_name="Почта покупателя")
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        ordering = ['-time_create', 'name']


class Provider(models.Model):
    title = models.CharField(max_length=150,verbose_name="Название")
    year_of_foundation = models.IntegerField(null=True,verbose_name="Год основания")
    number_of_buyers = models.IntegerField(null=True,verbose_name="Количество покупателей")
    car = models.ManyToManyField(CarType)
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['-time_create', 'title']

