from django.db import models
from core.models import TimeStampedModel

# Create your models here.


class FavList(TimeStampedModel):

    created_by = models.OneToOneField("users.User", on_delete=models.CASCADE)
    books = models.ManyToManyField("books.Book", related_name="fav_list")
    movies = models.ManyToManyField("movies.Movie", related_name="fav_list")

    def __str__(self):
        return self.created_by

    class Meta:
        verbose_name_plural = "FavList"
