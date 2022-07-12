from rest_framework import routers
from customer.views import CustomerViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'user', UserViewSet)


urlpatterns = router.urls