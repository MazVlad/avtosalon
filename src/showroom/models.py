from django.db import models
from django_countries.fields import CountryField
from src.car.models import Car
from src.core.models import BaseModel


def jsonfield_default_value():
    return [{'name': 'None'}, {'mileage': 0}, {'color': 'white'}, {'price': 0}]


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


class ShowroomDiscount(BaseModel):
    name = models.CharField(max_length=100)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()
    percent = models.DecimalField(decimal_places=2, max_digits=4)
    cars = models.ForeignKey("car.Car", null=True, on_delete=models.SET_NULL)
    showroom = models.ForeignKey("Showroom", null=True, on_delete=models.SET_NULL)


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
