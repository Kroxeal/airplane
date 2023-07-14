# Generated by Django 4.2.2 on 2023-07-14 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='airplane',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='route',
        ),
        migrations.RemoveField(
            model_name='ordersusers',
            name='order',
        ),
        migrations.RemoveField(
            model_name='ordersusers',
            name='seat',
        ),
        migrations.RemoveField(
            model_name='ordersusers',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='seats',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='seats',
            name='airplane',
        ),
        migrations.RemoveField(
            model_name='seats',
            name='user',
        ),
        migrations.RemoveField(
            model_name='users',
            name='orders_users_mtm',
        ),
        migrations.RemoveField(
            model_name='users',
            name='passport',
        ),
        migrations.DeleteModel(
            name='Airplanes',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='OrdersUsers',
        ),
        migrations.DeleteModel(
            name='Passports',
        ),
        migrations.DeleteModel(
            name='Routes',
        ),
        migrations.DeleteModel(
            name='Seats',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
