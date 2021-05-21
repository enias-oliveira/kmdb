from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication

from .models import Movie

from .serializers import MovieSerializer

from .permissions import IsAdminOrAnonReadOnly


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrAnonReadOnly]

    def list(self, request, *args, **kwargs):
        if not request.data:
            queryset = self.filter_queryset(self.get_queryset())

        queryset = self.get_queryset().filter(**request.data)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
