# Generated by Django 4.2.2 on 2023-06-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_remove_orders_price_remove_orders_seat_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passports',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='passports',
            name='date_of_expire',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='passports',
            name='date_of_issue',
            field=models.DateField(),
        ),
    ]
