import secret
import urllib2
import json

TMDB_BASE_URL = "https://api.themoviedb.org/3/"
TMDB_BASE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
YOUTUBE_BASE_URL = "https://www.youtube.com/watch?v="

_tmdb = None


class _TMDBClient:
    """A controller to handle calls to The Movie DB API"""

    def __init__(self):
        """The api_key is loaded from the secret file"""
        self.api_key = secret.TMDB_API_KEY

    @staticmethod
    def _query_tmdb_api(url):
        """
        A generic http GET call to a url expecting a JSON response
        """
        contents = {}
        try:
            response = urllib2.urlopen(url)
            contents = json.loads(response.read())  # Convert JSON to dict
        except urllib2.HTTPError as e:
            if e.code == 401:
                # Check that API key is valid in auth fails
                print("Unauthorized access - ensure you have set the correct TMDB api_key set in secret.py")
            elif e.code == 404:
                print("File not found for url: " + url)
            else:
                print(e)
        except:
            print("An unknown exception has ocurred")
        finally:
            return contents

    def get_movie_details(self, tmdb_id):
        """
        Makes the call to /movie/{movie_id} section of the api.
        A successful call returns numerous details regarding the movie, from which only the title and a poster path
        are returned.
        """
        url = TMDB_BASE_URL + "movie/" + str(tmdb_id) + "?api_key=" + self.api_key
        contents = self._query_tmdb_api(url)
        details = {}
        if "title" in contents:
            details["title"] = contents["title"]
        else:
            print ("Cannot find title for movie with id: " + tmdb_id)
        if "poster_path" in contents:
            if contents["poster_path"] != "":
                details["poster_path"] = TMDB_BASE_IMAGE_URL + contents["poster_path"]
        else:
            print ("Cannot find poster path for movie with id: " + tmdb_id)
        return details

    def get_movie_trailer_url(self, tmdb_id):
        """
        Get a list of trailer and return the first one that is :
         - A trailer
         - on YouTube
         - in English
        """
        url = TMDB_BASE_URL + "movie/" + str(tmdb_id) + "/videos?api_key=" + self.api_key
        contents = self._query_tmdb_api(url)
        link = ""

        if "results" in contents:
            for result in contents["results"]:
                if result["type"] == "Trailer" and result["site"] == "YouTube" and result["iso_639_1"] == "en":
                    link = YOUTUBE_BASE_URL + result["key"]
                    break
        if link == "":
            print("No videos returned for movie id: " + tmdb_id)
        return link


def tmdb_client():
    """
    Extremely simplictic singleton
    """
    global _tmdb
    if _tmdb is None:
        _tmdb = _TMDBClient()
    return _tmdb
