from rest_framework import serializers

from .models import Comment

from accounts.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(
        fields=("id", "first_name", "last_name"),
        read_only=True,
    )

    class Meta:
        model = Comment
        exclude = ["movie"]
