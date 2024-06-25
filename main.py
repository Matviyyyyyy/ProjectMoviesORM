import django_setup
from project2.models import Director, Genre, Movie, Actor, Theater, Screening, Ticket,Review
from datetime import date
from decimal import Decimal


while True:
    print("\n1. Додати актора")
    print("2. Додати фільм")
    print("3. Додати директора фільму")
    print("4. Додати показ фільму")
    print("5. Додати жанр фільму")
    print("6. Додати кінотеатр")
    print("7. Додати квиток")
    print("8. Додати відгук")
    print("9. Додати актора до фільму")
    print("10. Зробити певну операцію з таблицею відгуків")
    print("11. Вийти")

    choice = input("Оберіть опцію (1-11): ")

    if choice == "1":
        first_name = input("Вкажи ім'я актора")
        last_name = input("Вкажи прізвище актора")
        year_actor = int(input("Вкажи рік народження актора"))
        month_actor = int(input("Вкажи місяць народження актора"))
        day_actor = int(input("Вкажи день народження актора"))
        new_actor = Actor(first_name = first_name, last_name = last_name, birth_date = date(year_actor, month_actor, day_actor))
        new_actor.save()
        print("Актора додано!")
    if choice == "2":
        title = input("Вкажи назву фільму")
        duration = input("Вкажи тривалість фільму")
        genre_id = int(input("Вкажи id жанру фільму"))
        director_id = int(input("Вкажи id директора фільму"))
        genre_movie = Genre.objects.get(id = genre_id)
        director_movie = Director.objects.get(id=director_id)
        if genre_movie and director_movie:
            new_movie = Movie(title = title, duration=duration, genre_id=genre_movie, director_id=director_movie)
            new_movie.save()
            print("Фільм створено!")
        else:
            print("Жанр або режисера не знайдено")
    if choice == "4":
        movie_id = int(input("Вкажи id фільму"))
        screening_year = int(input("Рік показу"))
        screening_month = int(input("Місяць показу"))
        screening_day = int(input("День показу"))
        theater_id = int(input("id кінотеатру"))
        screen_movie = Movie.objects.get(id = movie_id)
        screen_theater = Theater.objects.get(id=theater_id)
        if screen_movie and screen_theater:
            new_screening = Screening(movie_id=screen_movie, screening_date = date(screening_year, screening_month, screening_day), theater_id=screen_theater)
            new_screening.save()
            print("Сеанс створено!")
        else:
            print("Театр або фільм не знайдено.")

    if choice == "3":
        first_name_director = input("Вкажи ім'я директора")
        last_name_director = input("Вкажи прізвище директора")
        year_actor_director = int(input("Вкажи рік народження директора"))
        month_actor_director = int(input("Вкажи місяць народження директора"))
        day_actor_director = int(input("Вкажи день народження директора"))
        new_director = Actor(first_name=first_name_director, last_name=last_name_director, birth_date=date(year_actor_director, month_actor_director, day_actor_director))
        new_director.save()
        print("Директора додано!")
    if choice == "5":
        name_genre = input("Назва жанру")
        new_genre = Genre(name=name_genre)
        new_genre.save()
        print("Жанр додано!")
    if choice == "6":
        name_theater = input("Назва кінотеатру")
        location_theater = input("Місце знаходження кінотеатру")
        capacity_theater = int(input("Вмісткість кінотеатру"))
        new_theater = Theater(name = name_theater, location = location_theater, capacity = capacity_theater)
        new_theater.save()
        print("Театр додано!")
    if choice == "7":
        screening_id_ticket = int(input("Id сеансу"))
        seat_number_ticket = input("Місце сидіння")
        price_ticket = input("Ціна квитка")
        screening_ticket = Screening.objects.get(id = screening_id_ticket)
        if screening_ticket:
            new_ticket = Ticket(screening_id = screening_ticket, seat_number = seat_number_ticket, price = price_ticket)
            new_ticket.save()
            print("Квиток додано!")
        else:
            print("Сеанс не знайдено")
    if choice == "8":
        movie_id_review = int(input("Id фільму"))
        reviewer_first_name = input("Ім'я рев'ювера")
        reviewer_last_name = input("Прізвище рев'ювера")
        rating = input("Рейтинг відгуку")
        comment = input("Вкажи текст відгуку")
        movie_review = Movie.objects.get(id = movie_id_review)
        if movie_review:
            new_review = Review(movie_id = movie_review, reviewer_first_name= reviewer_first_name, reviewer_last_name=reviewer_last_name, rating = rating, comment=comment)
            new_review.save()
            print("Відгук додано!")
        else:
            print("Шось не то")
    if choice == "9":
        id_actor = int(input("Id актора"))
        id_movie = int(input("Id фільму"))
        needed_actor = Actor.objects.get(id = id_actor)
        needed_movie = Movie.objects.get(id = id_movie)
        if needed_actor and needed_movie:
            needed_actor.movies.add(needed_movie)
            print("Актора додано до фільму!")
        else:
            print("Актора або фільм не знайдено.")
    if choice == "10":
        operations = input('''Обери операцію
        1 - видалити запиc,
        2 - змінити запис1
        ''')
        if operations == "1":
            id_deleted_review = int(input("Вкажи id відгуку,який хочеш видалити"))
            deleted_review = Review.objects.get(id = id_deleted_review)
            if deleted_review:
                deleted_review.delete()
            else:
                print("Некоректний id")
        if operations == "2":
            id_changed_review = int(input("Вкажи id відгуку,який хочеш змінити"))
            changed_review = Review.objects.get(id = id_changed_review)
            if changed_review:
                new_comment_for_review = input("Вкажи новий текст до відгуку")
                changed_review.comment = new_comment_for_review
                changed_review.save()
            else:
                print("Некоректний id")
    if choice == "11":
        break





