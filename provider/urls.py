from rest_framework import routers
from provider.views import ProviderViewSet, ProviderDiscountViewSet


router = routers.DefaultRouter()
router.register(r"provider", ProviderViewSet)
router.register(r"provider_discount", ProviderDiscountViewSet)


urlpatterns = router.urls
