from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=256)
    have_watched = models.BooleanField(default=False)