from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .serializers import UserSerializer, CustomAuthTokenSerializer

from rest_framework.authtoken.views import ObtainAuthToken


class AccountViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
