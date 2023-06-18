from django.db import models

# Create your models here.

SEX = [
    ("m", "male"),
    ("f", "female")
]


class Airplanes(models.Model):
    name = models.CharField(max_length=100)
    seat = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Orders(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    airplane = models.OneToOneField('Airplanes', on_delete=models.CASCADE)
    route = models.OneToOneField('Routes', on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user}"


class Users(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    passport = models.OneToOneField('Passports', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Passports(models.Model):
    passport_number = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    sex = models.CharField(max_length=1, choices=SEX)
    date_of_birth = models.DateTimeField(auto_now_add=True)
    date_of_issue = models.DateTimeField(auto_now_add=True)
    date_of_expire = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photo_user', null=True)

    def __str__(self):
        return f"{self.passport_number}"


class Routes(models.Model):
    country_departure = models.CharField(max_length=40)
    country_arrival = models.CharField(max_length=40)
    date_departure = models.DateTimeField(auto_now_add=True)
    date_arrival = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.country_departure}"
