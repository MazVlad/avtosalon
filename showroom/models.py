from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User


class CarManufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    CAR_TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('Coupe', 'Coupe'),
        ('Crossover', 'Crossover'),
        ('Hatchback','Hatchback'),
        ('Minivan', 'Minivan'),
    ]
    manufacturer = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=100, choices=CAR_TYPE_CHOICES,verbose_name="Вид авто")
    model = models.CharField(max_length=150, verbose_name="Модель авто")
    year = models.IntegerField(default=0,verbose_name="Год выпуска")
    price = models.FloatField(verbose_name="Цена авто")
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model


    class Meta:
        verbose_name = "Модель авто"
        verbose_name_plural = "Модели авто"
        ordering = ['-time_create', 'car_type']


class Showroom(models.Model):
    name = models.CharField(max_length=100,verbose_name="Название салона")
    location = CountryField(verbose_name="Местоположение")
    balance = models.DecimalField(decimal_places=2, max_digits=6,verbose_name="Баланс автосалона")
    cars = models.ManyToManyField(Car, blank=True)
    customers = models.ManyToManyField('Customer', blank=True)
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'
        ordering = ['-time_create', 'name']


class ShowroomDiscount(models.Model):
    name = models.CharField(max_length=100)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()
    percent = models.DecimalField(decimal_places=2, max_digits=4)
    cars = models.ManyToManyField(Car)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)


class ShowroomHistory(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Покупатель")
    balance = models.FloatField(verbose_name="Баланс")
    email = models.EmailField(max_length=254,verbose_name="Почта покупателя")
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        ordering = ['-time_create', 'user']


class CustomerHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)


class Provider(models.Model):
    name = models.CharField(max_length=150,verbose_name="Название")
    year_of_foundation = models.IntegerField(null=True,verbose_name="Год основания")
    cars = models.ManyToManyField(Car, blank=True)
    showrooms = models.ManyToManyField(Showroom, blank=True)
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['-time_create', 'name']


class ProviderDiscount(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

