from django.db import models
from core.models import TimeStampedModel

# Create your models here.


class Review(TimeStampedModel):

    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    text = models.TextField()
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, null=True, blank=True
    )
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, null=True, blank=True
    )
    rating = models.IntegerField()

    def __str__(self):
        return self.created_by

    class Meta:
        verbose_name_plural = "Review"
