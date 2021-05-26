from rest_framework import serializers

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
