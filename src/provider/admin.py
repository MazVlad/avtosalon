from django.contrib import admin
from src.provider.models import Provider, ProviderDiscount


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("name", "year_of_foundation")


@admin.register(ProviderDiscount)
class ProviderDiscountAdmin(admin.ModelAdmin):
    list_display = ["provider"]
