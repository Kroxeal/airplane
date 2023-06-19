from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.db.models import F
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register((Airplanes))
class AirplanesAdmin(admin.ModelAdmin):
    list_display = ['name', 'seat']


# class OrdersAdmin(admin.ModelAdmin):
#

@admin.register(Passports)
class PassportsAdmin(admin.ModelAdmin):
    list_display = ['passport_number', 'nationality', 'sex', 'date_of_birth', 'date_of_issue', 'date_of_expire', 'photo']
    # fields = ['passport_number', 'nationality', 'sex', 'date_of_birth', 'date_of_issue', 'date_of_expire', 'photo']
    list_editable = ['nationality', 'sex']
    list_filter = (
        ('nationality'),
    )
    ordering = ['sex', 'nationality']


@admin.register(Routes)
class RoutesAdmin(admin.ModelAdmin):
    list_display = ['country_departure', 'city_departure', 'country_arrival', 'city_arrival', 'date_departure', 'date_arrival', 'price']
    # fields =

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'passport']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['airplane', 'route']

@admin.register(OrdersUsers)
class OrdersUsersAdmin(admin.ModelAdmin):
    list_display = ['user', 'order']

# admin.site.register(Airplanes)
# admin.site.register(Orders)
# admin.site.register(Users)
# admin.site.register(Passports)
# admin.site.register(Routes)
# admin.site.register(OrdersUsers)
