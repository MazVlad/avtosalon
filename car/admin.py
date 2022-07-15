from django.contrib import admin
from car.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "manufacturer",
        "car_type",
        "model",
        "year",
        "color",
        "mileage",
        "engine_volume",
        "price",
    )
