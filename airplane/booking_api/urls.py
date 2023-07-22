from django.urls import path, re_path

from .views import AllUsersAPIView, RoutesAPIViewController, TemporaryAPIViewController

urlpatterns = [
    path('search_api', TemporaryAPIViewController.as_view(), name='search_api'),
    path('routes_api', RoutesAPIViewController.as_view(), name='routes_api'),
]