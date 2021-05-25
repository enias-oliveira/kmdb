from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication

from .models import Movie

from .serializers import MovieSerializer, MovieFiltersSerializer

from .permissions import IsAdminOrAnonReadOnly


class DynamicFilterMixin:
    def list(self, request, *args, **kwargs):

        serialized_fields = MovieFiltersSerializer(data=request.data)

        def get_filters(filter_data):
            return {
                f"{key}__contains": f"{value}" for (key, value) in filter_data.items()
            }

        if request.data and serialized_fields.is_valid(raise_exception=True):
            queryset = self.get_queryset().filter(**get_filters(request.data))
        else:
            queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MovieViewSet(DynamicFilterMixin, viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrAnonReadOnly]
