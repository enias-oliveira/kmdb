from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AccountViewSet, CustomObtainAuthToken

router = DefaultRouter()
router.register(r"accounts", AccountViewSet, basename="accounts")

urlpatterns = [
    path("login/", CustomObtainAuthToken.as_view()),
    path("", include(router.urls)),
]
