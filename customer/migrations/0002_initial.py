# Generated by Django 4.0.6 on 2022-07-13 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("customer", "0001_initial"),
        ("car", "0001_initial"),
        ("showroom", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customerhistory",
            name="showroom",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="showroom.showroom",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="cars",
            field=models.ManyToManyField(
                through="customer.CustomerHistory", to="car.car"
            ),
        ),
    ]
