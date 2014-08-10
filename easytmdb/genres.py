# -*- coding: utf-8 -*-
from base import TMDB


class Genres(TMDB):
    """

    See: http://docs.themoviedb.apiary.io/#genres
    """
    BASE_PATH = 'genre/'
    URLS = {
        'movie_list': 'movie/list',
        'tv_list': 'tv/list',
        'movies': '{id}/movies',
    }

    def __init__(self, id=0):
        self.id = id
        super(Genres, self).__init__()

    def movie_list(self, **kwargs):
        """Get the list of genres for movies.

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_path('movie_list')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def tv_list(self, **kwargs):
        """Get the list of genres for TV shows.

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_path('tv_list')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def movies(self, **kwargs):
        """Get the list of movies for a particular genre by id.

        By default, only movies with 10 or more votes are included.

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param include_all_movies: (optional) Toggle the inclusion of all movies
                                   and not just those with 10 or more ratings.
                                   Either `True` or `False`.
        :param include_adult: (optional) Toggle the inclusion of adult titles. Either `True`
                              or `false`.
        """
        path = self._get_id_path('movies')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response
