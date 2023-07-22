from django.urls import path, re_path

from booking.views import main, all_users

urlpatterns = [
    path('main/', main, name='main'),
    path('people/', all_users, name='people'),
]
