from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "genres",
            "launch",
            "classification",
            "synopsis",
        ]
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
