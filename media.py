import tmdb


class Movie:
    def __init__(self, tmdb_id):
        self.tmdb_id = tmdb_id
        self.title = ""
        self.poster_image_url = ""
        self.trailer_youtube_url = ""

    def load_tmdb_details(self):
        details = tmdb.tmdb_client().get_movie_details(self.tmdb_id)
        if {"title", "poster_path"} <= set(details):
            self.title = details["title"]
            self.poster_image_url = details["poster_path"]

    def load_movie_trailer(self):
        self.trailer_youtube_url = tmdb.tmdb_client().get_movie_trailer_url(self.tmdb_id)

    def is_ready_for_website(self):
        return self.title != "" and self.poster_image_url != "" and self.trailer_youtube_url != ""
