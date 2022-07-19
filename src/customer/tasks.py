from config.celery import app
from src.customer.models import Customer, CustomerHistory
from src.showroom.models import Showroom,ShowroomHistory
from django.db.models import Q


@app.task
def customers_buy_cars():
    for customer in Customer.objects.all():
        query = customer.query
        find_showroom_q = (Q(car__name__startswith=query[0].get('name')) &
                           Q(car__mileage__lte=query[1].get('mileage')) &
                           Q(car__width__gte=query[2].get('color')) &
                           Q(car__price__lte=query[3].get('price')))
        for showroom in Showroom.objects.all():
            if find_showroom_q == showroom.query:
                for x in showroom.cars.all():
                    if customer.cars == x and x.price <= customer.balance:
                        CustomerHistory.objects.create(
                            customer=customer.name,
                            showroom=showroom,
                            price=x.price,
                            car=customer.cars,
                        )
                        ShowroomHistory.objects.create(
                            car=customer.car, price=x.price, showroom=showroom
                        )
