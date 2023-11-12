from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UsersAPIViewSet

router = DefaultRouter()
router.register('user', UsersAPIViewSet, 'api_users')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="api_login"),
    path('refresh/', TokenRefreshView.as_view(), name="api_refresh"),
]

urlpatterns += router.urls