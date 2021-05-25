from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User


class Review(models.Model):
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )
    review = models.TextField()
    spoiler = models.BooleanField()

    critic = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        on_update=models.CASCADE,
    )
