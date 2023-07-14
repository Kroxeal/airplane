from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

SEX = [
    ("m", "male"),
    ("f", "female")
]

STATUS_CHOICES = [
    ("p", "paid"),
    ("n", "not paid"),
    ("r", "rejected")
]


class Aircrafts(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Orders(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.total_amount}"


class Users(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    passport = models.OneToOneField('Passports', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Passports(models.Model):
    passport_number = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    sex = models.CharField(max_length=1, choices=SEX)
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
    date_departure = models.DateTimeField()
    date_arrival = models.DateTimeField()
    price = models.PositiveIntegerField(default=328)
    aircraft = models.ForeignKey('Aircrafts', on_delete=models.CASCADE)

    def __str__(self):
        return f"from {self.country_departure} to {self.country_arrival}"


class Seats(models.Model):
    seat_number = models.IntegerField(null=True)
    aircraft = models.ForeignKey('Aircrafts', on_delete=models.CASCADE)
    order = models.ForeignKey('Orders', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('aircraft',
                           'seat_number',
                           )

    def __str__(self):
        return f"{self.seat_number}"


