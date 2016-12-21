import media
import fresh_tomatoes

MOVIE_ID_LIST = ["6977", "68718", "68735", "22954", "881", "286217", "330459", "278", "281957"]
movies = []


def create_movies():
    global movies
    for movie_id in MOVIE_ID_LIST:
        movie = media.Movie(movie_id)
        movies.append(movie)


def load_movies():
    global movies
    for movie in movies:
        movie.load_tmdb_details()
        movie.load_movie_trailer()


if __name__ == '__main__':
    create_movies()
    load_movies()

    fresh_tomatoes.open_movies_page(movies)
