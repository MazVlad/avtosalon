from config.celery import app
from src.customer.models import Customer, CustomerBuyCar, CustomerHistory
from src.showroom.models import Showroom, ShowroomSaleCar, ShowroomHistory
from django.db.models import Q


@app.task
def customers_buy_cars():
    for showroom in Showroom.objects.all():
        for customer in Customer.objects.all():
            query = customer.query
            find_showroom_q = (
                Q(car__name__startswith=query[0].get("name"))
                & Q(car__mileage__lte=query[1].get("mileage"))
                & Q(car__width__gte=query[2].get("color"))
                & Q(car__price__lte=query[3].get("price"))
            )
        showroom_sale = (
            ShowroomSaleCar.objects.filter(find_showroom_q)
            .order_by("-discount")
            .first()
        )
        customer_buy = (
            CustomerBuyCar.objects.filter(find_showroom_q).order_by("-discount").first()
        )
        if showroom_sale.car == customer_buy.car:
            CustomerHistory.objects.create(
                car=customer_buy.cars,
                showroom=showroom,
            )
        if customer.balance >= showroom_sale.car.price:
            customer.balance -= showroom_sale.car.price
            showroom_sale.provider.balance += showroom_sale.car.price
            CustomerHistory.objects.create(
                customer=customer.name,
                price=showroom_sale.car.price,
            )
            ShowroomHistory.objects.create(
                car=customer_buy.cars,
                price=showroom_sale.car.price,
                showroom=showroom,
            )
