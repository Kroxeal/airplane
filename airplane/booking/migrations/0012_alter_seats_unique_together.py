# Generated by Django 4.2.2 on 2023-07-09 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_seats_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seats',
            unique_together={('airplane', 'seat_number')},
        ),
    ]
