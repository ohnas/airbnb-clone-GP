from django.db import models
from core.models import TimeStampedModel

# Create your models here.


class Book(TimeStampedModel):

    title = models.CharField(max_length=50)
    year = models.IntegerField()
    cover_image = models.ImageField(null=True, blank=True)
    rating = models.IntegerField()
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="books"
    )
    writer = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Book"
