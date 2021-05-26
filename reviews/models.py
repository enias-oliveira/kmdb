from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User

from movies.models import Movie


class Review(models.Model):
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )
    review = models.TextField()
    spoilers = models.BooleanField()

    critic = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="criticism_set"
    )
