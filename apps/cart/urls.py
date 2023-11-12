from rest_framework.routers import DefaultRouter

from apps.cart.views import *

router = DefaultRouter()
router.register('cart', CartAPIViewSet, 'api_cart')
router.register('cart_item', CartItemAPIViewSet, 'api_cartitem')
router.register('wishlist', WishlistAPIViewSet, 'api_cart')
router.register('wishlist_item', WishlistItemAPIViewSet, 'api_cartitem')

urlpatterns = router.urls