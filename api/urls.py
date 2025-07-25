# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'points', views.PointDataViewSet, basename='pointdata')
router.register(r'polygons', views.PolygonDataViewSet, basename='polygondata')

urlpatterns = [
    path('', include(router.urls)),
]
