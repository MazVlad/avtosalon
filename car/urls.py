from rest_framework import routers
from car.views import CarManufacturerViewSet, CarViewSet


router = routers.DefaultRouter()
router.register(r'car_manufacturer', CarManufacturerViewSet)
router.register(r'cars', CarViewSet)


urlpatterns = router.urls