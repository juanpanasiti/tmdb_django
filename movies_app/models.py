from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.title} ({self.release_date})'