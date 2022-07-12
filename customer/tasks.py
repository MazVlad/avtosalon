from main.celery import app
from customer.models import Customer, CustomerOrder, CustomerHistory
from showroom.models import Showroom,ShowroomHistory


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