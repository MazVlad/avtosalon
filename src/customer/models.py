from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from src.core.models import BaseModel
from src.car.models import Car
from src.showroom.models import jsonfield_default_value


class Customer(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Customer name")
    balance = models.DecimalField(
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(9999999)],
        decimal_places=2,
        max_digits=10,
        verbose_name="Customer balance",
    )
    email = models.EmailField(max_length=254, verbose_name="Customer email")
    query = models.JSONField(blank=True, default=jsonfield_default_value)
    cars = models.ManyToManyField(Car, through="CustomerHistory")
    # m2m car throws CustomerHistory
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ["-created_at", "name"]


class CustomerHistory(BaseModel):
    car = models.ForeignKey("car.Car", null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    showroom = models.ForeignKey(
        "showroom.Showroom", null=True, on_delete=models.SET_NULL
    )


"""class CustomerOrder(BaseModel):
    car = models.ForeignKey('car.Car', null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey('Customer', null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.car}-{self.price}' """
