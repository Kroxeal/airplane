from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.db.models import F
from django.utils.safestring import mark_safe
# Register your models here.


class OrdersUsersIniline(admin.StackedInline):
    model = OrdersUsers


class UsersIniline(admin.StackedInline):
    model = Users


class PassportsInline(admin.StackedInline):
    model = Passports

@admin.display()
def get_html_photo(objects):
    if objects.photo:
        return mark_safe(f'<img src={objects.photo.url} width=50>')


@admin.register((Airplanes))
class AirplanesAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'seat',
                    ]


# class OrdersAdmin(admin.ModelAdmin):
#

@admin.register(Passports)
class PassportsAdmin(admin.ModelAdmin):
    list_display = ['passport_number',
                    'nationality', 'sex',
                    'date_of_birth', 'date_of_issue',
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
    list_filter = (
        ('nationality'),
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
                    ]
    list_editable = ['price']
    fields = ['country_departure',
              'city_departure',
              'country_arrival',
              'city_arrival',
              'date_departure',
              'date_arrival',
              'price',
              ]
    # fields =


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'surname',
                    'phone',
                    'email',
                    'passport',
                    ]
    list_editable = ['phone']
    list_display_links = ['name',
                          'passport',]
    # inlines = [
    #     PassportsInline,
    # ]



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['airplane',
                    'route',
                    ]
    inlines = [
        OrdersUsersIniline,
    ]


@admin.register(OrdersUsers)
class OrdersUsersAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'order',
                    ]

# admin.site.register(Airplanes)
# admin.site.register(Orders)
# admin.site.register(Users)
# admin.site.register(Passports)
# admin.site.register(Routes)
# admin.site.register(OrdersUsers)
