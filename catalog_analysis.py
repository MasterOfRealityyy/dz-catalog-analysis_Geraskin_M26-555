import math

movies = [
    {"title": "The Dune Chronicles",
     "year": 2021,
     "genres": {"sci-fi", "drama"},
     "rating": 8.6,
     "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories",
     "year": 2019,
     "genres": {"comedy", "drama"},
     "rating": 7.1,
     "duration_min": 98,
     "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours",
     "year": 2016,
     "genres": {"thriller", "drama"},
     "rating": 6.4,
     "duration_min": 112,
     "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers",
     "year": 2023,
     "genres": {"sci-fi", "action"},
     "rating": 5.9,
     "duration_min": 101,
     "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery",
     "year": 2014,
     "genres": {"comedy"},
     "rating": 7.8,
     "duration_min": 89,
     "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo",
     "year": 2020,
     "genres": {"thriller", "mystery"},
     "rating": 8.9,
     "duration_min": 124,
     "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static",
     "year": 2022,
     "genres": {"drama"},
     "rating": 4.8,
     "duration_min": 137,
     "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm",
     "year": 2024,
     "genres": {"sci-fi", "drama"},
     "rating": 9.2,
     "duration_min": 118,
     "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes",
     "year": 2011,
     "genres": {"comedy"},
     "rating": 6.0,
     "duration_min": 95,
     "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor",
     "year": 2018,
     "genres": {"action", "thriller"},
     "rating": 7.3,
     "duration_min": 129,
     "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    avg_rate = round(sum(i["rating"] for i in movies) / len(movies), 1)
    return avg_rate


def catalog_age_stats(movies, current_year=2026):
    movies_ages = [current_year - movie["year"] for movie in movies]
    oldest_movie = max(movies_ages)
    newest_movie = min(movies_ages)
    avg_age = math.ceil(sum(movies_ages) / len(movies_ages))
    return oldest_movie, newest_movie, avg_age


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif 7 <= rating <= 8.9:
        return "хорошо"
    return "средне" if 5 <= rating <= 6.9 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _ if year < 2015:
            return "старые"


def not_comedy():
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def first_masterpiece():
    k = 0
    while k < len(movies):
        if movies[k]["rating"] > 9.0:
            print(movies[k]["title"])
            break
        k += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    counter = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            counter += 1
    return counter


def normalize_title(title):
    words = title.split()
    result = " ".join([word[0].upper() + word[1:].lower() for word in words])
    return result


def make_slug(title):
    result = title.lower().replace(" ", "-")
    return result


def format_report_line(movie):
    return (f"\"{normalize_title(movie['title'])}\""
            f" ({movie['year']}) — {movie['rating']}/10, "
            f"{duration_in_hours(movie['duration_min'])}, "
            f"жанры: {', '.join(sorted(movie['genres']))}")


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [m["title"] for m in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(m["title"], m["rating"]) for m in sorted_movies[:n]]


def count_by_genre(movies):
    result = {}
    for movie in movies:
        for genre in movie["genres"]:
            result[genre] = result.get(genre, 0) + 1
    return result


def actor_filmography(movies):
    result = {}
    for movie in movies:
        for actor in movie["actors"]:
            result.setdefault(actor, []).append(movie["title"])
    return result


def movie_rate():
    avg = average_rating(movies)
    movie_rating = {movie["title"]: movie["rating"]
                    for movie in movies
                    if movie["rating"] > avg}
    print(movie_rating)


def all_genres(movies):
    result = set()
    for movie in movies:
        result.update(movie["genres"])
    return result


def common_actors(movie1, movie2):
    result = set(movie1["actors"]) & set(movie2["actors"])
    return result


def genres_only_in_one(movies_a, movies_b):
    result = all_genres(movies_a) - all_genres(movies_b)
    return result


def iter_high_rated(movies, min_rating=8.0):
    for m in movies:
        if m["rating"] >= min_rating:
            yield m


def lazy_output():
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))


def generator_duration_min():
    print(sum(m["duration_min"] for m in movies if m["rating"] > 7))


def build_report(movies):
    print(f"ОТЧЕТ ПО КАТАЛОГУ\n"
          f"Средний рейтинг: {average_rating(movies)}\n"
          f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет\n"
          f"\n"
          f"Топ-3 фильма: ")

    top_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)[:3]

    for movie in top_movies:
        print(f"  {format_report_line(movie)}")

    genre_count = count_by_genre(movies)
    print("\nФильмов по жанрам:")
    for genre, count in sorted(genre_count.items(), key=lambda kv: kv[1], reverse=True):
        print(f"  {genre} — {count}")

    print(f"\nВсе жанры каталога: {', '.join(sorted(all_genres(movies)))}")


if __name__ == "__main__":
    build_report(movies)
