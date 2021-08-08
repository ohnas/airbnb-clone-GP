from django.db import models
from core.models import TimeStampedModel

# Create your models here.


class Movie(TimeStampedModel):

    title = models.CharField(max_length=50)
    year = models.IntegerField()
    cover_image = models.ImageField(null=True, blank=True)
    rating = models.IntegerField()
    category = models.ManyToManyField("categories.Category", related_name="movies")
    director = models.ForeignKey("people.Person", on_delete=models.CASCADE)
    cast = models.ManyToManyField("people.Person", related_name="movies")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Movie"
