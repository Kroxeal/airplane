# Generated by Django 4.2.2 on 2023-06-19 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_orders_route_alter_routes_country_arrival_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routes',
            name='date_arrival',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='routes',
            name='date_departure',
            field=models.DateTimeField(),
        ),
    ]
