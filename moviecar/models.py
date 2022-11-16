from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=256)
    review = models.CharField(max_length=1024, default="")
    img = models.CharField(max_length=1024, default="#")
    rating = models.IntegerField(default=0)
    have_watched = models.BooleanField(default=False)