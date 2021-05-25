from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.response import Response

from .models import Review

from .serializers import ReviewSerializer

from .permissions import IsAdminOrAnonReadOnly


class ReviewView(GenericAPIView, CreateModelMixin, UpdateModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
