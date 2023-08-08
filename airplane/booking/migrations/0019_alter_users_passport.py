# Generated by Django 4.2.2 on 2023-08-07 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0018_temporary_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='passport',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passport_users', to='booking.passports'),
        ),
    ]
