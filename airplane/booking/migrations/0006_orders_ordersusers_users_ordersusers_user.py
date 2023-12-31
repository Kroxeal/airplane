# Generated by Django 4.2.2 on 2023-06-19 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_remove_users_passport_delete_orders_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airplane', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking.airplanes')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('orders_users_mtm', models.ManyToManyField(through='booking.OrdersUsers', to='booking.orders')),
                ('passport', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking.passports')),
            ],
        ),
        migrations.AddField(
            model_name='ordersusers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.users'),
        ),
    ]
