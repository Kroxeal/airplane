from django.contrib import admin
from django.utils.html import format_html
from django.db.models import F
from django.utils.safestring import mark_safe

from booking.models import Passports, Users, Seats, Routes, Aircrafts, Orders, Airlines, Temporary


class RoutesInlines(admin.StackedInline):
    model = Routes


class OrdersInline(admin.StackedInline):
    model = Orders


class SeatsInline(admin.StackedInline):
    model = Seats


class UsersInline(admin.StackedInline):
    model = Users


class PassportsInline(admin.StackedInline):
    model = Passports


@admin.display()
def get_html_photo(objects):
    if objects.photo:
        return mark_safe(f'<img src={objects.photo.url} width=50>')


@admin.register(Temporary)
class TemporaryDataAdmin(admin.ModelAdmin):
    list_display = [
        'iata_departure',
        'iata_arrival',
        'date_departure',
    ]


@admin.register(Airlines)
class AirlinesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'iata_airline',
    ]
    list_editable = [
        'iata_airline',
    ]


@admin.register(Aircrafts)
class AircraftsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'iata_aircraft',
        'amount',
    ]
    list_editable = [
        'amount',
        'iata_aircraft',
    ]
    inlines = [
        RoutesInlines,
        SeatsInline,
    ]


@admin.register(Passports)
class PassportsAdmin(admin.ModelAdmin):
    list_display = [
        'passport_number',
        'nationality',
        'sex',
        'date_of_birth',
        'date_of_issue',
        'date_of_expire',
    ]
    fields = [
        'passport_number',
        'nationality',
        'sex',
        'date_of_birth',
        'date_of_issue',
        'date_of_expire',
    ]
    list_editable = [
        'nationality',
        'sex',
    ]
    list_filter = [
        'nationality',
    ]
    inlines = [
        UsersInline,
    ]
    ordering = [
        'sex',
        'nationality',
    ]


@admin.register(Routes)
class RoutesAdmin(admin.ModelAdmin):
    list_display = [
        'country_departure',
        'city_departure',
        'country_arrival',
        'city_arrival',
        'date_arrival',
        'price',
        'aircraft',
    ]
    list_editable = [
        'price',
    ]
    fields = [
        'country_departure',
        'city_departure',
        'country_arrival',
        'city_arrival',
        'date_arrival',
        'price',
        'aircraft',
        'airline',
    ]


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'surname',
        'phone',
        'email',
        'passport',
    ]
    list_editable = [
        'phone',
    ]
    list_display_links = [
        'name',
        'passport',
    ]
    inlines = [
        OrdersInline,
    ]


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'date',
        'status',
        'total_amount',
    ]
    list_editable = [
        'total_amount',
    ]
    inlines = [
        SeatsInline,
    ]


@admin.register(Seats)
class SeatsAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'seat_number',
        'aircraft',
    ]



