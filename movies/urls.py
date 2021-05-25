from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

from reviews.urls import router as review_router

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movies")

urlpatterns = [
    path("", include(router.urls)),
    path("movies/<int:pk>/", include(review_router.urls)),
]
