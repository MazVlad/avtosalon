from django.db import models
from django.contrib.auth.models import User
from core.models import abstract_models

class Customer(abstract_models.Abstract):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Customer name")
    balance = models.FloatField(null=True,verbose_name="Customer balance")
    email = models.EmailField(max_length=254,verbose_name="Customer email")


    def __str__(self):
        return self.user


    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['-created_at', 'user']


class CustomerHistory(models.Model):
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    showroom = models.ForeignKey('showroom.Showroom',null=True, on_delete=models.SET_NULL)


class CustomerOrder(models.Model):
    car = models.ForeignKey('car.Car',null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey('Customer',null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.car}-{self.price}'
