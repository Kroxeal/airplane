# Generated by Django 4.2.2 on 2023-06-18 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplanes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('seat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Passports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_number', models.CharField(max_length=40)),
                ('nationality', models.CharField(max_length=40)),
                ('sex', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1)),
                ('date_of_birth', models.DateTimeField(auto_now_add=True)),
                ('date_of_issue', models.DateTimeField(auto_now_add=True)),
                ('date_of_expire', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(null=True, upload_to='photo_user')),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_departure', models.CharField(max_length=40)),
                ('country_arrival', models.CharField(max_length=40)),
                ('date_departure', models.DateTimeField(auto_now_add=True)),
                ('date_arrival', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('passport_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking.passports')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.PositiveIntegerField(null=True)),
                ('price', models.PositiveIntegerField()),
                ('airplane_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking.airplanes')),
                ('route_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking.routes')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.users')),
            ],
        ),
    ]
