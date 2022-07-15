from main.celery import app
from customer.models import Customer, CustomerHistory
from showroom.models import Showroom, ShowroomHistory


@app.task
def customers_buy_cars():
    for order in Customer.objects.all():
        for showroom in Showroom.objects.all():
            if order.query == showroom.query:
                for x in showroom.cars.all():
                    if order.cars == x and x.price <= order.balance:
                        CustomerHistory.objects.create(
                            customer=order.customer,
                            showroom=showroom,
                            price=x.price,
                            car=order.car,
                        )

                        ShowroomHistory.objects.create(
                            car=order.car, price=x.price, showroom=showroom
                        )
