from django.db import models

class CarManufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    CAR_TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('Coupe', 'Coupe'),
        ('Crossover', 'Crossover'),
        ('Hatchback','Hatchback'),
        ('Minivan', 'Minivan'),
    ] # core
    manufacturer = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=100, choices=CAR_TYPE_CHOICES,verbose_name="Car type")
    model = models.CharField(max_length=150, verbose_name="Model")
    year = models.IntegerField(default=0,verbose_name="Year of release") # 1900+
    price = models.FloatField(verbose_name="Car price")# positive
    is_active = models.BooleanField(default=True) # abs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model


    class Meta:
        verbose_name = "Car model"
        verbose_name_plural = "Car models"
        ordering = ['-created_at', 'car_type']

