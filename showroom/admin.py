from django.contrib import admin
from showroom.models import Showroom, ShowroomDiscount, ShowroomHistory


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "balance")


@admin.register(ShowroomDiscount)
class ShowroomDiscountAdmin(admin.ModelAdmin):
    list_display = ("name", "start_at", "end_at", "percent", "cars", "showroom")


@admin.register(ShowroomHistory)
class ShowroomHistoryAdmin(admin.ModelAdmin):
    list_display = ("car", "price", "showroom", "provider")
