from django.db import models
from django_countries.fields import CountryField
from car.models import Car


class Showroom(models.Model):
    name = models.CharField(max_length=100,verbose_name="Showroom name")
    location = CountryField(verbose_name="Location")
    balance = models.DecimalField(decimal_places=2, max_digits=6,verbose_name="Showroom balance",null=True)
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
    showroom = models.ForeignKey('showroom.Showroom', on_delete=models.CASCADE)
    provider = models.ForeignKey('provider.Provider', on_delete=models.CASCADE)
