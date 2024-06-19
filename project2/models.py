from django.db import models

# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=300)
    birth_date = models.DateField()
class Genre(models.Model):
    name = models.CharField(max_length=300)
class Movie(models.Model):
    title = models.CharField(max_length=300)
    duration = models.CharField(max_length=100)
    genre_id = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    director_id = models.ForeignKey(Director, on_delete=models.DO_NOTHING)

class Actor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=300)
    birth_date = models.DateField()
    movies = models.ManyToManyField("Movie")

class Theater(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    capacity = models.IntegerField()

class Screening(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    screening_date = models.DateField()
    theater_id = models.ForeignKey(Theater, on_delete=models.DO_NOTHING)

class Ticket(models.Model):
    screening_id  = models.ForeignKey(Screening, on_delete=models.DO_NOTHING)
    seat_number = models.IntegerField()
    price = models.CharField(max_length=100)

class Review(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    reviewer_first_name = models.CharField(max_length=200)
    reviewer_last_name = models.CharField(max_length=300)
    rating = models.CharField(max_length=100)
    comment = models.TextField()

