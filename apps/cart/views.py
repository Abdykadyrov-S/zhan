from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.cart.models import *
from apps.cart.serializers import *
from apps.products.models import Products

class CartAPIViewSet(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemAPIViewSet(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
class WishlistAPIViewSet(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

class WishlistItemAPIViewSet(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer

