# -*- coding: utf-8 -*-
import json

import requests

api_key = None
version = '3'


class TMDB(object):
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json'}

    def __init__(self):
        self.url = 'https://api.themoviedb.org/{version}'.format(version=version)

    def get_url(self, path):
        return '{base}/{path}'.format(base=self.url, path=path)

    def get_params(self, params):
        api_dict = {'api_key': api_key}
        if params:
            params.update(api_dict)
        else:
            params = api_dict
        return params

    def _get(self, path, params=None):
        url = self.get_url(path)
        params = self.get_params(params)

        response = requests.get(url, params=params, headers=self.headers)

        return json.loads(response.content.decode('utf-8'))

    def _post(self, path, params=None, payload=None):
        url = self.get_url(path)
        params = self.get_params(params)
        if not payload:
            payload = {}

        response = requests.post(url, params=params, data=json.dumps(payload), headers=self.headers)

        return json.loads(response.content.decode('utf-8'))

    def _delete(self, path, params=None, payload=None):
        url = self.get_url(path)
        params = self.get_params(params)
        if not payload:
            payload = {}

        response = requests.delete(url, params=params, data=json.dumps(payload), headers=self.headers)

        return json.loads(response.content.decode('utf-8'))

    #
    # Set attributes to dictionary values.
    # - e.g.
    # >>> tmdb = TMDB()
    # >>> movie = tmdb.Movie(103332)
    # >>> response = movie.info()
    # >>> movie.title  # instead of response['title']
    #
    def _set_attrs_to_values(self, response={}):
        for key in response.keys():
            setattr(self, key, response[key])


class Movies(TMDB):
    """Interact with The Movie Database Movies endpoints

    See: http://docs.themoviedb.apiary.io/#movies
    """

    def __init__(self, id=0):
        super(Movies, self).__init__()
        self.id = id

    def info(self, params={}):
        """Get the basic movie information for a specific movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = 'movie' + '/' + str(self.id)
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    def alternative_titles(self, params={}):
        """Get the alternative titles for a specific movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Falternative_titles

        :param country: (optional) ISO 3166-1 code, e.g. 'us'. For a list of
                        3166-1 codes, see http://en.wikipedia.org/wiki/ISO_3166-1
        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = 'movie' + '/' + str(self.id) + '/alternative_titles'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    def credits(self):
        """Get the cast and crew information for a specific movie id.

        TMDB docs: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fcredits

        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = 'movie' + '/' + str(self.id) + '/credits'
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    def images(self, params={}):
        """Get the images (posters and backdrops) for a specific movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fimages

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param include_image_language: (optional) Comma separated ISO 639-1 codes,
                                       e.g. 'en, es'.
        :param append_to_response: (optional) Any Movies method names, comma
                                   separated, e.g. 'credits, images'.
        """
        path = 'movie' + '/' + str(self.id) + '/images'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    def keywords(self):
        """Get the plot keywords for a specific movie id.

        TMDB docs: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fkeywords

        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = 'movie' + '/' + str(self.id) + '/keywords'
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    def releases(self):
        """Get the release date by country for a specific movie id.

        TMDB docs: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Freleases

        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = 'movie' + '/' + str(self.id) + '/releases'
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    def trailers(self):
        """Get the trailers for a specific movie id.

        TMDB docs: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Ftrailers

        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = 'movie' + '/' + str(self.id) + '/trailers'
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    def translations(self):
        """Get the translations for a specific movie id.

        TMDB docs: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Ftranslations

        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = 'movie' + '/' + str(self.id) + '/translations'
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    def similar_movies(self, params={}):
        """Get the similar movies for a specific movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fsimilar_movies

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = 'movie' + '/' + str(self.id) + '/similar_movies'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    def reviews(self, params={}):
        """Get the reviews for a particular movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Freviews

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = 'movie' + '/' + str(self.id) + '/reviews'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    def lists(self, params={}):
        """Get the lists that the movie belongs to.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Flists

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = 'movie' + '/' + str(self.id) + '/lists'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    def changes(self, params={}):
        """Get the changes for a specific movie id.

        Changes are grouped by key, and ordered by date in descending order. By
        default, only the last 24 hours of changes are returned. The maximum number
        of days that can be returned in a single request is 14. The language is
        present on fields that are translatable.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fchanges

        :param start_date: (optional) A string in the format 'YYYY-MM-DD'
        :param end_date: (optional) Same as start_date
        """
        path = 'movie' + '/' + str(self.id) + '/changes'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    def latest(self):
        """Get the latest movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Flatest
        """
        path = 'movie/latest'
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    def upcoming(self, params={}):
        """Get the list of upcoming movies.

        This list refreshes every day. The maximum number of items this list will include is 100.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Fupcoming

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = 'movie/upcoming'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    def now_playing(self, params={}):
        """Get the list of movies playing in theatres.

        This list refreshes every day. The maximum number of items this list will include is 100.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Fnow_playing

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = 'movie/now_playing'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    def popular(self, params={}):
        """Get the list of popular movies on The Movie Database.

        This list refreshes every day.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Fpopular

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = 'movie/popular'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    def top_rated(self, params={}):
        """Get the list of top rated movies.

        This list refreshes every day. This list only includes movies that have
        10 or more votes.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Ftop_rated

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = 'movie/top_rated'
        response = self._get('movie' + '/top_rated', params)
        self._set_attrs_to_values(response)
        return response

    def account_states(self, params):
        """Get status of whether or not the movie has been rated or added to favourite or watch lists.

        A `valid session <https://www.themoviedb.org/documentation/api/sessions>`_ id is required.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Faccount_states

        :param session_id: A session id as returned from :py:func:session_new
        """
        path = 'movie' + '/' + str(self.id) + '/account_states'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    def rating(self, params, json_body):
        """Rate a movie.

        A `valid session <https://www.themoviedb.org/documentation/api/sessions>`_
        id or guest session id is required.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Flists

        :param page: (optional) Result page number, e.g. 3.
        """
        path = 'movie' + '/' + str(self.id) + '/rating'
        response = self._post(path, params, json_body)
        self._set_attrs_to_values(response)
        return response
