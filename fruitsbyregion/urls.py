from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from region.views import RegionViewsets
from fruit.views import FruitViewsets

router = DefaultRouter()
router.register(r'regions', RegionViewsets)
router.register(r'fruits', FruitViewsets)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
