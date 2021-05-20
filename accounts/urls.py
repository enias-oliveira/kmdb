from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import AccountViewSet

router = DefaultRouter()
router.register(r"accounts", AccountViewSet, basename="accounts")

urlpatterns = [
    path("login/", views.obtain_auth_token),
    path("", include(router.urls)),
]
