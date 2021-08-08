from django.db import models
from core.models import TimeStampedModel

# Create your models here.


class Category(TimeStampedModel):

    KIND_BOOK = "book"
    KIND_MOVIE = "movie"
    KIND_BOTH = "both"

    KIND_CHOICES = ((KIND_BOOK, "Book"), (KIND_MOVIE, "Movie"), (KIND_BOTH, "Both"))

    name = models.CharField(max_length=20)
    kind = models.CharField(choices=KIND_CHOICES, max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"

