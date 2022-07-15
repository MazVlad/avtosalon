from main.celery import app
from showroom.models import Showroom
from provider.models import Provider


@app.task
def showroom_buy_car():
    for showroom in Showroom.objects.all():
        for provider in Provider.objects.all():
            for car in provider.cars.all():
                if showroom.query == car.query:
                    showroom.cars.add(car)
                    provider.showrooms.add(showroom)
            provider.save()
        showroom.save()
        print(showroom, showroom.cars.all())
