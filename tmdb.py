import secret
import urllib2, json

TMDB_BASE_URL = "https://api.themoviedb.org/3/"
TMDB_BASE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
YOUTUBE_BASE_URL = "https://www.youtube.com/watch?v="

_tmdb = None

class _TMDBClient:
    def __init__(self):
        self.api_key = secret.TMDB_API_KEY

    def _query_tmdb_api(self, url):
        contents = {}
        try:
            response = urllib2.urlopen(url)
            contents = json.loads(response.read())
        except urllib2.HTTPError as e:
            if e.code == 401:
                print("Unauthorized access - ensure you have set the correct TMDB api_key set in secret.py")
            elif e.code == 404:
                print("File not found for url: " + url)
            else:
                print(e)
        except:
            print("An unknown exception has ocurred")
        finally:
            return contents

    def get_movie_details(self, id):
        url = TMDB_BASE_URL+"movie/" + str(id) + "?api_key=" + self.api_key
        contents = self._query_tmdb_api(url)
        details = {}
        if "title" in contents:
            details["title"] = contents["title"]
        else:
            print ("Cannot find title for movie with id: " + id)
        if "poster_path" in contents:
            if contents["poster_path"] != "":
                details["poster_path"] = TMDB_BASE_IMAGE_URL + contents["poster_path"]
        else:
            print ("Cannot find poster path for movie with id: " + id)
        return details

    def get_movie_trailer_url(self, id):
            url = TMDB_BASE_URL + "movie/" + str(id) + "/videos?api_key=" + self.api_key
            contents = self._query_tmdb_api(url)
            link = ""
            if "results" in contents:
                for result in contents["results"]:
                    if result["name"] == "Official Trailer":
                        link = YOUTUBE_BASE_URL+result["key"]
                        break
            if link == "":
                print("No videos returned for movie id: " + id)
            return link

def tmdb_client():
    global _tmdb
    if _tmdb is None:
        _tmdb = _TMDBClient()
    return _tmdb