# -*- coding: utf-8 -*-
import json

import requests

api_key = None
version = '3'


class TMDB(object):
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json'}
    BASE_PATH = ''
    URLS = {}

    def __init__(self):
        self.url = 'https://api.themoviedb.org/{version}'.format(version=version)

    def _get_path(self, key):
        return self.BASE_PATH + self.URLS[key]

    def _get_id_path(self, key):
        return self._get_path().format(id=self.id)

    def _get_complete_url(self, path):
        return '{base}/{path}'.format(base=self.url, path=path)

    def _get_params(self, params):
        api_dict = {'api_key': api_key}
        if params:
            params.update(api_dict)
        else:
            params = api_dict
        return params

    def _get(self, path, params=None):
        url = self._get_complete_url(path)
        params = self._get_params(params)

        response = requests.get(url, params=params, headers=self.headers)

        return json.loads(response.content.decode('utf-8'))

    def _post(self, path, params=None, payload=None):
        url = self._get_complete_url(path)
        params = self._get_params(params)
        if not payload:
            payload = {}

        response = requests.post(url, params=params, data=json.dumps(payload), headers=self.headers)

        return json.loads(response.content.decode('utf-8'))

    def _delete(self, path, params=None, payload=None):
        url = self._get_complete_url(path)
        params = self._get_params(params)
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
