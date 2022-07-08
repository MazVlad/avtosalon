from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Customer name")
    balance = models.FloatField(null=True,verbose_name="Customer balance")
    email = models.EmailField(max_length=254,verbose_name="Customer email")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['-created_at', 'user']


class CustomerHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    showroom = models.ForeignKey('showroom.Showroom', on_delete=models.CASCADE)
