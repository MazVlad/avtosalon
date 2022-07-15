from rest_framework import routers
from car.views import CarViewSet


router = routers.DefaultRouter()
router.register(r"cars", CarViewSet)


urlpatterns = router.urls
