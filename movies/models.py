from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    duration = models.CharField(max_length=50)
    rated_as = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100, null=True, blank=True)
    rating = models.CharField(max_length=50)
    stars = models.TextField()
    streaming_on = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.year})"
