# Generated by Django 4.2.2 on 2023-07-09 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_seats_orders_seat_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='seat_number',
        ),
    ]