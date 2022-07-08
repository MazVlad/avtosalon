from django.db import models
from django_countries.fields import CountryField
from car.models import Car


class Showroom(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=100,verbose_name="Название салона")
    location = CountryField(verbose_name="Местоположение")
    balance = models.DecimalField(decimal_places=2, max_digits=6,verbose_name="Баланс автосалона",null=True)
=======
    name = models.CharField(max_length=100,verbose_name="Showroom name")
    location = CountryField(verbose_name="Location")
    balance = models.DecimalField(decimal_places=2, max_digits=6,verbose_name="Showroom balance",null=True)
>>>>>>> feature/api
    cars = models.ManyToManyField(Car, blank=True)
    customers = models.ManyToManyField('customer.Customer', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Showroom'
        verbose_name_plural = 'Showrooms'
        ordering = ['-created_at', 'name']


class ShowroomDiscount(models.Model):
    name = models.CharField(max_length=100)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()
    percent = models.DecimalField(decimal_places=2, max_digits=4)
    cars = models.ManyToManyField('car.Car')
    showroom = models.ForeignKey('Showroom', on_delete=models.CASCADE)


class ShowroomHistory(models.Model):
    car = models.ForeignKey('car.Car', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=6)
<<<<<<< HEAD
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Покупатель")
    balance = models.FloatField(null=True,verbose_name="Баланс")
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

=======
    showroom = models.ForeignKey('showroom.Showroom', on_delete=models.CASCADE)
    provider = models.ForeignKey('provider.Provider', on_delete=models.CASCADE)
>>>>>>> feature/api


