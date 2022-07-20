from django.db import models
from src.core.models import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from src.car.models import Car


class Provider(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Provider name")
    year_of_foundation = models.IntegerField(
        null=True, verbose_name="Year of foundation"
    )
    cars = models.ManyToManyField("car.Car", through="ProviderSale")
    showrooms = models.ManyToManyField("showroom.Showroom", blank=True)
    balance = models.DecimalField(
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(999999)],
        decimal_places=2,
        max_digits=10,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"
        ordering = ["-created_at", "name"]


class ProviderSale(BaseModel):
    """Provider sells cars to the showroom"""

    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name="supplier_cars"
    )
    count = models.PositiveIntegerField(default=1)
    car = models.ForeignKey("car.Car", on_delete=models.SET_NULL, null=True)
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
    )
