from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser

from booking.enums import SexTypes, StatusChoices


class Aircrafts(models.Model):
    name = models.CharField(max_length=100)
    iata_aircraft = models.CharField(max_length=20, default='733')
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Orders(models.Model):
    user = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
        related_name='user_orders',
    )
    total_amount = models.IntegerField()
    date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=StatusChoices.choices)

    def __str__(self):
        return f"{self.total_amount}"


class Users(AbstractUser):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    passport = models.OneToOneField(
        'Passports',
        on_delete=models.CASCADE,
        related_name='passport_users',
        null=True,
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='booking_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='booking_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.username}"


class Passports(models.Model):
    passport_number = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    sex = models.CharField(max_length=10, choices=SexTypes.choices)
    date_of_birth = models.DateField()
    date_of_issue = models.DateField()
    date_of_expire = models.DateField()
    photo = models.ImageField(upload_to='photo_user', null=True)

    def __str__(self):
        return f"{self.passport_number}"


class Routes(models.Model):
    country_departure = models.CharField(max_length=40, default='Belarus')
    country_arrival = models.CharField(max_length=40, default='Poland')
    city_departure = models.CharField(max_length=40, default='Minsk')
    city_arrival = models.CharField(max_length=40, default='Warsaw')
    date_arrival = models.DateField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        validators=[MinValueValidator(0.0)],
    )
    aircraft = models.ForeignKey(
        'Aircrafts',
        on_delete=models.CASCADE,
        related_name='aircraft_route',
    )
    airline = models.ForeignKey(
        'Airlines',
        on_delete=models.CASCADE,
        related_name='airline_route',
    )
    temporary = models.OneToOneField(
        'Temporary',
        on_delete=models.CASCADE,
        related_name='temporary_route'
    )
    user = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
        related_name='user_route',
    )

    def __str__(self):
        return f"from {self.country_departure} to {self.country_arrival}"


class Seats(models.Model):
    seat_number = models.IntegerField(null=True)
    aircraft = models.ForeignKey(
        'Aircrafts',
        on_delete=models.CASCADE,
        related_name='aircraft_seat',
    )
    order = models.ForeignKey(
        'Orders',
        on_delete=models.CASCADE,
        related_name='order_seat',
    )

    class Meta:
        unique_together = ('aircraft',
                           'seat_number',
                           )

    def __str__(self):
        return f"{self.seat_number}"


class Airlines(models.Model):
    name = models.CharField(max_length=50)
    iata_airline = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.name}"


class Temporary(models.Model):
    iata_departure = models.CharField(max_length=20)
    iata_arrival = models.CharField(max_length=20)
    date_departure = models.DateField()

    user = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
        related_name='user_temporary',
    )

    def __str__(self):
        return f"{self.iata_departure}"
