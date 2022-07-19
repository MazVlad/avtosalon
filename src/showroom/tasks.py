from config.celery import app
from src.showroom.models import Showroom,ShowroomHistory
from src.provider.models import Provider
from django.db.models import Q


'''@app.task
def showroom_buy_car():
    for showroom in Showroom.objects.all():
        for provider in Provider.objects.all():
            for car in provider.cars.all():
                if showroom.query == car.query:
                    showroom.cars.add(car)
                    provider.showrooms.add(showroom)
            provider.save()
        showroom.save()
        print(showroom, showroom.cars.all())'''


@app.task
def showroom_buy_car():
    for showroom in Showroom.objects.all():
        query = showroom.query
        find_provider_q = (Q(car__name__startswith=query[0].get('name')) &
                           Q(car__mileage__lte=query[1].get('mileage')) &
                           Q(car__width__gte=query[2].get('color')) &
                           Q(car__price__lte=query[3].get('price')))
        for provider in Provider.objects.all():
            if find_provider_q == provider:
                ShowroomHistory.objects.create(provider=provider)
