from decimal import Decimal
from django.db import models
from core.enums.car import CarType
from core.models import abstract_models
from django.core.validators import MaxValueValidator, MinValueValidator

class CarManufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Car(abstract_models.Abstract):
    manufacturer = models.ForeignKey(CarManufacturer,null=True, on_delete=models.SET_NULL)
    car_type = models.CharField(max_length=100,verbose_name="Car type", choices=CarType.choices())
    model = models.CharField(max_length=150, verbose_name="Model")
    year = models.IntegerField(default=0,verbose_name="Year of release",validators=[MinValueValidator(1900),
                                       MaxValueValidator(2022)])
    price = models.DecimalField(decimal_places=2, max_digits=10,verbose_name="Car price",validators=[MinValueValidator(Decimal('0.01'))])


    def __str__(self):
        return self.model


    class Meta:
        verbose_name = "Car model"
        verbose_name_plural = "Car models"
        ordering = ['-created_at', 'car_type']

