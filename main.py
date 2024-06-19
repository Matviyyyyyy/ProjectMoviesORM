import django_setup
from project2.models import Director, Genre, Movie, Actor, Theater, Screening, Ticket,Review
from datetime import date
from decimal import Decimal


director1 = Director(
    first_name = "Chris",
    last_name = "Columbus",
    birth_date = date(1958, 9, 10)
)
director1.save()

genre1 = Genre(
    name = "Adventure"
)
genre1.save()

movie1 = Movie(
    title = "Harry Potter",
    duration = "2.53",
    genre_id = genre1,
    director_id = director1
)
movie1.save()

actor1 = Actor(
    first_name = "Daniel",
    last_name = "Radcliffe",
    birth_date = date(1989, 7, 23)
)
actor1.save()
actor1.movies.add(movie1)


theater1 = Theater(
    name = "Planet of Kinos",
    location = "ТРЦ «Forum Lviv», вулиця Під Дубом, 7Б",
    capacity = 20
)
theater1.save()

screen1 = Screening(
    movie_id = movie1,
    screening_date = date(2024, 7, 1),
    theater_id = theater1
)
screen1.save()

ticket1 = Ticket(
    screening_id = screen1,
    seat_number = 1,
    price = "800.00"
)
ticket1.save()

ticket2 = Ticket(
    screening_id = screen1,
    seat_number = 2,
    price = "800.00"
)
ticket2.save()

ticket3 = Ticket(
    screening_id = screen1,
    seat_number = 3,
    price = "800.00"
)
ticket3.save()

ticket4 = Ticket(
    screening_id = screen1,
    seat_number = 4,
    price = "800.00"
)
ticket4.save()

ticket5 = Ticket(
    screening_id = screen1,
    seat_number = 5,
    price = "800.00"
)
ticket5.save()

ticket6 = Ticket(
    screening_id = screen1,
    seat_number = 6,
    price = "800.00"
)
ticket6.save()

ticket7 = Ticket(
    screening_id = screen1,
    seat_number = 7,
    price = "800.00"
)
ticket7.save()

ticket8 = Ticket(
    screening_id = screen1,
    seat_number = 8,
    price = "800.00"
)
ticket8.save()

ticket9 = Ticket(
    screening_id = screen1,
    seat_number = 9,
    price = "800.00"
)
ticket9.save()

ticket10 = Ticket(
    screening_id = screen1,
    seat_number = 10,
    price = "800.00"
)
ticket10.save()

ticket11 = Ticket(
    screening_id = screen1,
    seat_number = 11,
    price = "800.00"
)
ticket11.save()

ticket12 = Ticket(
    screening_id = screen1,
    seat_number = 12,
    price = "800.00"
)
ticket12.save()

ticket13 = Ticket(
    screening_id = screen1,
    seat_number = 13,
    price = "800.00"
)
ticket13.save()

ticket14 = Ticket(
    screening_id = screen1,
    seat_number = 14,
    price = "800.00"
)
ticket14.save()

ticket15 = Ticket(
    screening_id = screen1,
    seat_number = 15,
    price = "800.00"
)
ticket15.save()

ticket16 = Ticket(
    screening_id = screen1,
    seat_number = 16,
    price = "800.00"
)
ticket16.save()

ticket17 = Ticket(
    screening_id = screen1,
    seat_number = 17,
    price = "800.00"
)
ticket17.save()

ticket18 = Ticket(
    screening_id = screen1,
    seat_number = 18,
    price = "800.00"
)
ticket18.save()

ticket19 = Ticket(
    screening_id = screen1,
    seat_number = 19,
    price = "800.00"
)
ticket19.save()

ticket20 = Ticket(
    screening_id = screen1,
    seat_number = 20,
    price = "800.00"
)
ticket20.save()

review1 = Review(
    movie_id = movie1,
    reviewer_first_name = "Matviy",
    reviewer_last_name = "Gura",
    rating = "99.99",
    comment = "It's absolutely cool film about magic and another world"
)

review1.save()
