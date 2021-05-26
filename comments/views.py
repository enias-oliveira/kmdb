from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework.authentication import TokenAuthentication

from .models import Comment
from .serializers import CommentSerializer

from .permissions import IsStandardUser

from movies.models import Movie


class NestedCommentCreateModelMixin(
    CreateModelMixin,
):
    def create(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            movie = Movie.objects.get(id=pk)
        except Exception:
            return Response(
                {"detail": "Not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        comment = Comment.objects.create(
            **serializer.data, user=request.user, movie=movie
        )

        serialized_comment = CommentSerializer(comment)
        headers = self.get_success_headers(serialized_comment.data)

        return Response(
            serialized_comment.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class CommentViewSet(
    NestedCommentCreateModelMixin,
    GenericViewSet,
):
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStandardUser]

    def put(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            movie = Movie.objects.get(id=pk)
            comment = Comment.objects.filter(
                movie=movie,
                id=request.data["comment_id"],
            )

            if not comment:
                raise Exception()

        except Exception:
            return Response(
                {"detail": "Not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        comment = Comment.objects.filter(
            movie=movie,
            id=request.data["comment_id"],
        )

        comment.update(**serializer.data)

        serialized_comment = CommentSerializer(comment.first())

        return Response(serialized_comment.data)
