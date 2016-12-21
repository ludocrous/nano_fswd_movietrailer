import tmdb


class Movie:
    """A representation of a movie, complete with title and links to poster and trailer """
    def __init__(self, tmdb_id):
        self.tmdb_id = tmdb_id
        self.title = ""
        self.poster_image_url = ""
        self.trailer_youtube_url = ""

    def load_tmdb_details(self):
        """This functions calls to the tmdb client to obtain the movie title and its poster path """
        details = tmdb.tmdb_client().get_movie_details(self.tmdb_id)
        if {"title", "poster_path"} <= set(details):  # ensure both keys are in the results dict.
            self.title = details["title"]
            self.poster_image_url = details["poster_path"]

    def load_movie_trailer(self):
        """This functions calls to the tmdb client to obtain a url to a viable YouTube trailer"""
        self.trailer_youtube_url = tmdb.tmdb_client().get_movie_trailer_url(self.tmdb_id)

    def is_ready_for_website(self):
        """Only if all 3 properties have values is the movie object viable for inclusion in the html page """
        return self.title != "" and self.poster_image_url != "" and self.trailer_youtube_url != ""
