# Generated by Django 4.0.4 on 2022-05-18 13:02

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя покупателя')),
                ('balance', models.FloatField(verbose_name='Баланс')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта покупателя')),
                ('is_active', models.BooleanField(default=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
                'ordering': ['-time_create', 'name'],
            },
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(max_length=100, verbose_name='Вид авто')),
                ('title', models.CharField(max_length=150, verbose_name='Название авто')),
                ('year', models.IntegerField(default=0, max_length=10, verbose_name='Год выпуска')),
                ('price', models.FloatField(verbose_name='Цена авто')),
                ('is_active', models.BooleanField(default=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Вид авто',
                'verbose_name_plural': 'Виды авто',
                'ordering': ['-time_create', 'car_type'],
            },
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название салона')),
                ('location', django_countries.fields.CountryField(max_length=2, verbose_name='Местоположение')),
                ('number_of_cars', models.IntegerField(null=True, verbose_name='Количество авто')),
                ('is_active', models.BooleanField(default=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('car', models.ManyToManyField(to='avtosalon.cartype')),
            ],
            options={
                'verbose_name': 'Салон',
                'verbose_name_plural': 'Салоны',
                'ordering': ['-time_create', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('year_of_foundation', models.IntegerField(null=True, verbose_name='Год основания')),
                ('number_of_buyers', models.IntegerField(null=True, verbose_name='Количество покупателей')),
                ('is_active', models.BooleanField(default=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('car', models.ManyToManyField(to='avtosalon.cartype')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
                'ordering': ['-time_create', 'title'],
            },
        ),
    ]
