from django.db import models
from src.core.models import BaseModel


class Provider(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Provider name")
    year_of_foundation = models.IntegerField(
        null=True, verbose_name="Year of foundation"
    )
    cars = models.ManyToManyField("car.Car", blank=True)
    showrooms = models.ManyToManyField("showroom.Showroom", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"
        ordering = ["-created_at", "name"]


class ProviderDiscount(BaseModel):
    provider = models.ForeignKey(
        "provider.Provider", null=True, on_delete=models.SET_NULL
    )
