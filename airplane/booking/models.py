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
    # user = models.ForeignKey('Users', on_delete=models.CASCADE)
    airplane = models.OneToOneField('Airplanes', on_delete=models.CASCADE)
    route = models.OneToOneField('Routes', on_delete=models.CASCADE, null=True)
    # seat_number = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.airplane}"


class OrdersUsers(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    order = models.ForeignKey('Orders', on_delete=models.CASCADE)


class Users(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    passport = models.OneToOneField('Passports', on_delete=models.CASCADE)
    orders_users_mtm = models.ManyToManyField('Orders', through='OrdersUsers')

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
    date_departure = models.DateTimeField(auto_now_add=True)
    date_arrival = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField(default=328)

    def __str__(self):
        return f"from {self.country_departure} to {self.country_arrival}"
