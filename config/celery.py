import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "showroom_buy_car": {
        "task": "src.showroom.tasks.showroom_buy_car",
        "schedule": crontab(minute="*/10"),
    },
    "customer_buy_car": {
        "task": "src.customer.tasks.customers_buy_cars",
        "schedule": crontab(minute="*/50"),
    },
}
