# Generated by Django 4.0.6 on 2022-07-13 12:29

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("manufacturer", models.CharField(max_length=100, null=True)),
                (
                    "car_type",
                    models.CharField(
                        choices=[
                            ("SEDAN", "Sedan"),
                            ("COUPE", "Coupe"),
                            ("CROSSOVER", "Crossover"),
                            ("HATCHBACK", "Hatchback"),
                            ("MINIVAN", "Minivan"),
                        ],
                        max_length=100,
                        verbose_name="Car type",
                    ),
                ),
                ("model", models.CharField(max_length=150, verbose_name="Model")),
                (
                    "year",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(1900),
                            django.core.validators.MaxValueValidator(2022),
                        ],
                        verbose_name="Year of release",
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("RED", "Red"),
                            ("ORANGE", "Orange"),
                            ("YELLOW", "Yellow"),
                            ("GREEN", "Green"),
                            ("BLUE", "Blue"),
                            ("PURPLE", "Purple"),
                            ("PINK", "Pink"),
                            ("BLACK", "Black"),
                            ("WHITE", "White"),
                            ("GRAY", "Gray"),
                        ],
                        default="white",
                        max_length=100,
                        verbose_name="Car color",
                    ),
                ),
                (
                    "mileage",
                    models.PositiveIntegerField(default=0, verbose_name="Car mileage"),
                ),
                (
                    "engine_volume",
                    models.FloatField(null=True, verbose_name="Engine volume"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.01"))
                        ],
                        verbose_name="Car price",
                    ),
                ),
            ],
            options={
                "verbose_name": "Car model",
                "verbose_name_plural": "Car models",
                "ordering": ["-created_at", "car_type"],
            },
        ),
    ]
