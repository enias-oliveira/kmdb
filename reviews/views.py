from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework.authentication import TokenAuthentication

from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsCritic

from movies.models import Movie


class NestedReviewCreateModelMixin(
    CreateModelMixin,
):
    def create(self, request, pk, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if Movie.objects.filter(
            criticism_set__critic_id=request.user.id, id=pk
        ).exists():
            return Response(
                {"detail": "You already made this review."},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        try:
            movie = Movie.objects.get(id=pk)
        except Exception:
            return Response(
                {"detail": "Not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        review = Review.objects.create(
            **serializer.data, critic=request.user, movie=movie
        )

        serialized_review = ReviewSerializer(review)
        headers = self.get_success_headers(serialized_review.data)

        return Response(
            serialized_review.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class ReviewViewSet(
    NestedReviewCreateModelMixin,
    GenericViewSet,
):
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCritic]

    def put(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            movie = Movie.objects.get(id=pk)
            review = Review.objects.filter(movie=movie)

            if not review:
                raise Exception()

        except Exception:
            return Response(
                {"detail": "Not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        review.update(**serializer.data)

        serialized_review = ReviewSerializer(review.first())

        return Response(serialized_review.data)
