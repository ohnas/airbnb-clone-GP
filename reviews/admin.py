from django.contrib import admin
from reviews.models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ("created_by", "text", "movie", "book", "rating")

    list_filter = ("created_by", "text", "movie", "book", "rating")

