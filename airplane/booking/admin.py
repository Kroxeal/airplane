from django.contrib import admin
from .models import Passports, Users, Seats, Routes, Aircrafts, Orders
from django.utils.html import format_html
from django.db.models import F
from django.utils.safestring import mark_safe
# Register your models here.


class RoutesInlines(admin.StackedInline):
    model = Routes


class OrdersInline(admin.StackedInline):
    model = Orders


class SeatsInline(admin.StackedInline):
    model = Seats


class UsersIniline(admin.StackedInline):
    model = Users


class PassportsInline(admin.StackedInline):
    model = Passports


@admin.display()
def get_html_photo(objects):
    if objects.photo:
        return mark_safe(f'<img src={objects.photo.url} width=50>')


@admin.register(Aircrafts)
class AircraftsAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'amount',
                    ]
    list_editable = ['amount',
                     ]
    inlines = [RoutesInlines,
               SeatsInline,
               ]


@admin.register(Passports)
class PassportsAdmin(admin.ModelAdmin):
    list_display = ['passport_number',
                    'nationality',
                    'sex',
                    'date_of_birth',
                    'date_of_issue',
                    'date_of_expire',
                    ]
    fields = ['passport_number',
              'nationality',
              'sex',
              'date_of_birth',
              'date_of_issue',
              'date_of_expire',
              ]
    list_editable = ['nationality',
                     'sex',
                     ]
    list_filter = ('nationality',
                   )
    inlines = [
        UsersIniline,
        ]
    ordering = ['sex',
                'nationality',
                ]


@admin.register(Routes)
class RoutesAdmin(admin.ModelAdmin):
    list_display = ['country_departure',
                    'city_departure',
                    'country_arrival',
                    'city_arrival',
                    'date_departure',
                    'date_arrival',
                    'price',
                    'aircraft',
                    ]
    list_editable = [
        'price',
        ]
    fields = ['country_departure',
              'city_departure',
              'country_arrival',
              'city_arrival',
              'date_departure',
              'date_arrival',
              'price',
              'aircraft',
              ]


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'surname',
                    'phone',
                    'email',
                    'passport',
                    ]
    list_editable = [
        'phone',
        ]
    list_display_links = ['name',
                          'passport',
                          ]
    inlines = [OrdersInline,
               ]


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'date',
                    'status',
                    'total_amount',
                    ]
    list_editable = ['total_amount',
                     ]
    inlines = [SeatsInline,
               ]


@admin.register(Seats)
class SeatsAdmin(admin.ModelAdmin):
    list_display = ['order',
                    'seat_number',
                    'aircraft',
                    ]



