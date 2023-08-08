from rest_framework import routers
from django.urls import path, include, re_path

from booking_api.views import RoutesViewSet, TemporaryViewSet, RoutesDetailViewSet, SeatsViewSet, TemporaryAPIViewSet, \
    TemporaryAPIAllViewSet

router = routers.DefaultRouter()
router.register(r'temporary', TemporaryViewSet, basename='temporary')
router.register(r'routes', RoutesViewSet, basename='routes')
router.register(r'routes_detail', RoutesDetailViewSet, basename='routes_deatail')
router.register(r'seats', SeatsViewSet, basename='seats')
router.register(r'temporary_api', TemporaryAPIViewSet, basename='temporary_api')
router.register(r'temporary_api_all', TemporaryAPIAllViewSet, basename='temporary_api_all')

urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls')),
    re_path(r'^auth/', include('djoser.urls')),
]
