"""
tmdbsimple.py is a wrapper for The Movie Database API.
Refer to the official API documentation for more information.
http://docs.themoviedb.apiary.io/

Created by Celia Oakley on 2013-10-31.
"""

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


#
# Movies
# http://docs.themoviedb.apiary.io/#movies
#
class Movies(TMDB):

    """ """

    def __init__(self, id=0):
        super(Movies, self).__init__()
        self.id = id

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid}
    # optional parameters: language
    def info(self, params={}):
        path = 'movie' + '/' + str(self.id)
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    # http://preview.tinyurl.com/get-movie-alternative-titles
    # optional parameters: country
    def alternative_titles(self, params={}):
        path = 'movie' + '/' + str(self.id) + '/alternative_titles'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fcredits
    def credits(self):
        path = 'movie' + '/' + str(self.id) + '/credits'
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fimages
    # optional parameters: language
    def images(self, params={}):
        path = 'movie' + '/' + str(self.id) + '/images'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fkeywords
    def keywords(self):
        path = 'movie' + '/' + str(self.id) + '/keywords'
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Freleases
    def releases(self):
        path = 'movie' + '/' + str(self.id) + '/releases'
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Ftrailers
    def trailers(self):
        path = 'movie' + '/' + str(self.id) + '/trailers'
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    # http://preview.tinyurl.com/get-movie-translations
    def translations(self):
        path = 'movie' + '/' + str(self.id) + '/translations'
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    # http://preview.tinyurl.com/get-movie-similar-movies
    # optional parameters: page, language
    def similar_movies(self, params={}):
        path = 'movie' + '/' + str(self.id) + '/similar_movies'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Freviews
    # optional parameters: page, language
    def reviews(self, params={}):
        path = 'movie' + '/' + str(self.id) + '/reviews'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Flists
    # optional parameters: page, language
    def lists(self, params={}):
        path = 'movie' + '/' + str(self.id) + '/lists'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fchanges
    # optional parameters: start_date, end_date
    def changes(self, params={}):
        path = 'movie' + '/' + str(self.id) + '/changes'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Flatest
    def latest(self):
        path = 'movie/latest'
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Fupcoming
    # optional parameters: page, language
    def upcoming(self, params={}):
        path = 'movie/upcoming'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Fnow_playing
    # optional parameters: page, language
    def now_playing(self, params={}):
        path = 'movie/now_playing'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Fpopular
    # optional parameters: page, language
    def popular(self, params={}):
        path = 'movie/popular'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Ftop_rated
    # optional parameters: page, language
    def top_rated(self, params={}):
        path = 'movie/top_rated'
        response = self._get('movie' + '/top_rated', params)
        self._set_attrs_to_values(response)
        return response

    # http://preview.tinyurl.com/get-movie-account-states
    # required parameters: session_id
    def account_states(self, params):
        path = 'movie' + '/' + str(self.id) + '/account_states'
        response = self._get(path, params)
        self._set_attrs_to_values(response)
        return response

    # http://docs.themoviedb.apiary.io/#post-%2F3%2Fmovie%2F%7Bid%7D%2Frating
    # required parameters: session_id or guest_session_id
    # required JSON body: value
    def rating(self, params, json_body):
        path = 'movie' + '/' + str(self.id) + '/rating'
        response = self._post(path, params, json_body)
        self._set_attrs_to_values(response)
        return response
