from config.celery import app
from src.showroom.models import (
    Showroom,
    ShowroomBuyCar,
    ShowroomSaleCar,
    ShowroomHistory,
)
from src.provider.models import Provider, ProviderSale
from django.db.models import Q


"""@app.task
def showroom_buy_car():
    for showroom in Showroom.objects.all():
        for provider in Provider.objects.all():
            for car in provider.cars.all():
                if showroom.query == car.query:
                    showroom.cars.add(car)
                    provider.showrooms.add(showroom)
            provider.save()
        showroom.save()
        print(showroom, showroom.cars.all())"""


@app.task
def showroom_buy_car():
    for provider in Provider.objects.all():
        for showroom in Showroom.objects.all():
            query = showroom.query
            find_provider_q = (
                Q(car__name__startswith=query[0].get("name"))
                & Q(car__mileage__lte=query[1].get("mileage"))
                & Q(car__width__gte=query[2].get("color"))
                & Q(car__price__lte=query[3].get("price"))
            )
            provider_sale = (
                ProviderSale.objects.filter(find_provider_q)
                .order_by("-discount")
                .first()
            )
            showroom_buy = (
                ShowroomBuyCar.objects.filter(find_provider_q)
                .order_by("-discount")
                .first()
            )
            if showroom_buy.discount == provider_sale:
                ShowroomHistory.objects.create(provider=provider)
            if showroom.balance >= provider_sale.car.price:
                showroom.balance -= provider_sale.car.price
                provider_sale.provider.balance += provider_sale.car.price
                showroom.save()
                provider.save()
