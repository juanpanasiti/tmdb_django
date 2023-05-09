from django.test import TestCase

from .models import Movie

# Create your tests here.
class MovieModelTestCase(TestCase):
    def test_movie_creation(self):
        Movie.objects.create(title="The Godfather", description="An epic crime film", release_date="1972-03-14")
        self.assertEqual(Movie.objects.count(), 1)


    def test_movie_read(self):
        Movie.objects.create(title="The Godfather", description="An epic crime film", release_date="1972-03-14")
        movies = Movie.objects.all()
        self.assertGreaterEqual(len(movies), 1)
