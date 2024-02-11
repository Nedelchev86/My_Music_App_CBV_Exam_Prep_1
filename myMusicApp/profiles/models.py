from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from myMusicApp.profiles.validators import string_validator


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2), string_validator, ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
