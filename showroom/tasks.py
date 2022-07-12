from main.celery import app
from showroom.models import Showroom
from provider.models import Provider

@app.task
def customers_buy_cars():
    for order in CustomerOrder.objects.all():
        for showroom in Showroom.objects.all():
            for x in showroom.cars.all():
                if order.car == x and x.price <= order.price:
                    CustomerHistory.objects.create(customer=order.customer,
                                                   showroom=showroom,
                                                   price=x.price,
                                                   car=order.car)

                    ShowroomHistory.objects.create(car=order.car,
                                                   price=x.price,
                                                   showroom=showroom)


@app.task
def showroom_buy_car():
    for showroom in Showroom.objects.all():
        for provider in Provider.objects.all():
            for car in provider.cars.all():
                showroom.cars.add(car)
                showroom.save()