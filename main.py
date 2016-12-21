import media
import fresh_tomatoes
import secret

# This is a list of The Movie DB id's (https://www.themoviedb.org) for a selection of movies.
# This list of movies will be displayed on the webpage assuming they have valid entries.
MOVIE_ID_LIST = ["6977", "68718", "68735", "22954", "881", "286217", "330459", "278", "281957"]
movies = []


def create_movies():
    """Create the Movie instances and populate global list"""
    global movies
    for movie_id in MOVIE_ID_LIST:
        movie = media.Movie(movie_id)
        movies.append(movie)


def load_movies():
    """For each movie load the properties from The Movie DB"""
    global movies
    for movie in movies:
        movie.load_tmdb_details()
        movie.load_movie_trailer()


if __name__ == '__main__':
    if secret.TMDB_API_KEY == "ADD TMDB API KEY HERE":
        print "This application requires an api_key from The Movie DB (https://www.themoviedb.org)."
        print "This key must be set in secret.py"
        exit(0)
    create_movies()
    load_movies()
    fresh_tomatoes.open_movies_page(movies)
