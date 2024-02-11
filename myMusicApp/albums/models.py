from django.core.validators import MinValueValidator
from django.db import models

from myMusicApp.profiles.models import Profile

# from myMusicApp.profiles.models import Profile

# Create your models here.


GENRES = (
    ("pop", "Pop Music"),
    ("jazz", "Jazz Music"),
    ("rnb", "R&B Music"),
    ("rock", "Rock Music"),
    ("country", "Country Music"),
    ("dance", "Dance Music"),
    ("hiphop", "Hip Hop Music"),
    ("other", "Other"),
)


class Album(models.Model):
    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30,
    )

    artist = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    genre = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        choices=GENRES
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(0.0),),
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="albums"
    )
