from decimal import Decimal
from django.db import models
from core.enums.car import CarType, Color
from core.models import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator


class Car(BaseModel):
    manufacturer = models.CharField(max_length=100, null=True)
    car_type = models.CharField(
        max_length=100, verbose_name="Car type", choices=CarType.choices()
    )
    model = models.CharField(max_length=150, verbose_name="Model")
    year = models.PositiveIntegerField(
        default=0,
        verbose_name="Year of release",
        validators=[MinValueValidator(1900), MaxValueValidator(2022)],
    )
    color = models.CharField(
        max_length=100,
        default="white",
        blank=True,
        choices=Color.choices(),
        verbose_name="Car color",
    )
    mileage = models.PositiveIntegerField(default=0, verbose_name="Car mileage")
    engine_volume = models.FloatField(null=True, verbose_name="Engine volume")
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Car price",
        validators=[MinValueValidator(Decimal("0.01"))],
    )

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "Car model"
        verbose_name_plural = "Car models"
        ordering = ["-created_at", "car_type"]
