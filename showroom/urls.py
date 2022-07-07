from showroom.views import ShowroomViewSet,ShowroomDiscountViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'showroom', ShowroomViewSet)
router.register(r'showroom_discount', ShowroomDiscountViewSet)


urlpatterns = router.urls