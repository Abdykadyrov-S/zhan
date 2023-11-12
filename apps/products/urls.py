from rest_framework.routers import DefaultRouter

from apps.products.views import ProductsAPIViewSet, ReviewAPIViewSet

router = DefaultRouter()
router.register('products', ProductsAPIViewSet, 'api_products')
router.register('review', ReviewAPIViewSet, 'api_review')

urlpatterns = router.urls