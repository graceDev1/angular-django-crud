from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=256)
    year = models.IntegerField()
