from rest_framework import serializers

from .models import Review

from accounts.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    critic = UserSerializer(fields=("id", "first_name", "last_name"))

    class Meta:
        model = Review
        fields = "__all__"
        depth = 1
