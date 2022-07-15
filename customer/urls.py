from rest_framework import routers
from customer.views import CustomerViewSet


router = routers.DefaultRouter()
router.register(r"customer", CustomerViewSet)


urlpatterns = router.urls
