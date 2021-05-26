from rest_framework import serializers
from .models import Movie, Genre

from reviews.serializers import ReviewSerializer
from comments.serializers import CommentSerializer


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    criticism_set = ReviewSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        requested_genres = validated_data.pop("genres")
        selected_genres = [
            Genre.objects.get_or_create(name=req_genre["name"])[0]
            for req_genre in requested_genres
        ]

        movie = Movie.objects.create(**validated_data)
        movie.genres.set(selected_genres)

        return movie


class MovieFiltersSerializer(serializers.Serializer):
    title = serializers.CharField()
