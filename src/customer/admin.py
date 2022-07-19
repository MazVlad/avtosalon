from django.contrib import admin
from src.customer.models import Customer, CustomerHistory


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "balance", "email", "query")


@admin.register(CustomerHistory)
class CustomerHistoryAdmin(admin.ModelAdmin):
    list_display = ("car", "price", "customer", "showroom")
