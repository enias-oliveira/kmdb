from rest_framework import serializers
from django.contrib.auth.models import User

from movies.models import Movie
from .models import Review

from accounts.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    critic = UserSerializer(
        fields=("id", "first_name", "last_name"),
        read_only=True,
    )

    class Meta:
        model = Review
        exclude = ["movie"]
