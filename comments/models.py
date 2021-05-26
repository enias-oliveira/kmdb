from django.db import models

from django.contrib.auth.models import User

from movies.models import Movie


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
    )
