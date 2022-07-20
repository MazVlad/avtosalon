from django.db import models
from django_countries.fields import CountryField
from src.car.models import Car
from src.provider.models import Provider
from src.core.models import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator


def jsonfield_default_value():
    return [{"name": "None"}, {"mileage": 0}, {"color": "white"}, {"price": 0}]


class Showroom(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Showroom name")
    location = CountryField(verbose_name="Location")
    balance = models.DecimalField(
        decimal_places=2, max_digits=6, verbose_name="Showroom balance", null=True
    )
    cars = models.ManyToManyField(Car, blank=True, through="ShowroomHistory")
    customers = models.ManyToManyField("customer.Customer", blank=True)
    query = models.JSONField(blank=True, default=jsonfield_default_value)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Showroom"
        verbose_name_plural = "Showrooms"
        ordering = ["-created_at", "name"]


class ShowroomBuyCar(BaseModel):
    """showroom buying a car from a provider"""

    count = models.PositiveIntegerField(default=1)
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
    )
    car = models.ForeignKey("car.Car", on_delete=models.SET_NULL, null=True)
    car_showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE, null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)


class ShowroomSaleCar(BaseModel):
    """Showroom sells cars to the customer"""

    car = models.ForeignKey("car.Car", on_delete=models.SET_NULL, null=True)
    car_showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE, null=True)
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
    )


class ShowroomHistory(BaseModel):
    car = models.ForeignKey("car.Car", null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    showroom = models.ForeignKey(
        "showroom.Showroom", null=True, on_delete=models.SET_NULL
    )
    provider = models.ForeignKey(
        "provider.Provider", null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return str(self.car)
