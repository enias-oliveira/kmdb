from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication

from .models import Movie

from .serializers import MovieSerializer

from .permissions import IsAdminOrAnonReadOnly


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrAnonReadOnly]
