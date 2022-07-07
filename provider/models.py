from django.db import models
from car.models import Car
from showroom.models import Showroom


class Provider(models.Model):
    name = models.CharField(max_length=150,verbose_name="Provider name")
    year_of_foundation = models.IntegerField(null=True,verbose_name="Year of foundation")
    cars = models.ManyToManyField('car.Car', blank=True)
    showrooms = models.ManyToManyField('showroom.Showroom', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'
        ordering = ['-created_at', 'name']


class ProviderDiscount(models.Model):
    provider = models.ForeignKey('provider.Provider', on_delete=models.CASCADE)