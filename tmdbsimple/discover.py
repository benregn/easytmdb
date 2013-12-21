# -*- coding: utf-8 -*-
from base import TMDB


class Discover(TMDB):
    """Discover

    See: http://docs.themoviedb.apiary.io/#discover
    """
    BASE_PATH = 'discover/'
    URLS = {
        'movie': 'movie',
        'tv': 'tv',
    }

    def __init__(self):
        super(Discover, self).__init__()

    def _replace_underscore(self, dictionary):
        """Replace the last '_' (underscore) with a '.'' (dot)."""
        for key in dictionary:
            if 'gte' in key or 'lte' in key:
                new_key = '.'.join(key.rsplit('_', 1))
                dictionary[new_key] = dictionary.pop(key)

    def movie(self, **kwargs):
        """Discover movies by different types of data like average rating,
        number of votes, genres and certifications.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fdiscover%2Fmovie

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param sort_by: (optional) Available options are `vote_average.desc`,
                        `vote_average.asc`, `release_date.desc`, `release_date.asc`,
                        `popularity.desc`, `popularity.asc`.
        :param include_adult: (optional) Toggle the inclusion of adult titles.
                              Expected value is a boolean, `True` or `False`.
        :param year: (optional) Filter the results release dates to matches
                     that include this value.
        :param primary_release_year: (optional) Filter the results so that only
                                     the primary release date year has this
                                     value.
        :param with_genres: (optional) Only include movies with the specified
                            genres. Expected value is an integer (the id of a
                            genre). Multiple values can be specified. Comma
                            separated indicates an 'AND' query, while a pipe
                            (|) separated value indicates an 'OR'.
        :param vote_count_gte: (optional) Only include movies that are equal
                               to, or have a vote count higher than this value.
                               Expected value is an integer.
        :param vote_average_gte: (optional) Only include movies that are equal
                                 to, or have a higher average rating than this
                                 value. Expected value is a float.
        :param release_date_gte: (optional) The minimum release date to include.
                                 Expected format is YYYY-MM-DD.
        :param release_date_lte: (optional) The maximum release date to include.
                                 Expected format is YYYY-MM-DD.
        :param certification_country: (optional) Only include movies with
                                      certifications for a specific country.
                                      When this value is specified,
                                      `certification.lte` is required. A ISO
                                      3166-1 is expected.
        :param certification_lte: (optional) Only include movies with this
                                  certification and lower. Expected value is a
                                  valid certification for the specificed
                                  `certification_country`.
        :param with_companies: (optional) Filter movies to include a specific
                               company. Expected value is an integer (the id of
                               a company). They can be comma separated to
                               indicate an 'AND' query.
        """
        path = self._get_path('movie')

        self._replace_underscore(kwargs)

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def tv(self, **kwargs):
        """Discover TV shows by different types of data like average rating,
        number of votes, genres, the network they aired on and air dates.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fdiscover%2Ftv

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param sort_by: (optional) Available options are `vote_average.desc`,
                        `vote_average.asc`, `first_air_date.desc`,
                        `first_air_date.asc`, `popularity.desc`,
                        `popularity.asc`.
        :param first_air_date_year: (optional) Filter the results release dates
                                    to matches that include this value. Expected
                                    value is a year.
        :param vote_count.gte: (optional) Only include TV shows that are equal
                               to, or have a vote count higher than this value.
                               Expected value is an integer.
        :param vote_average.gte: (optional) Only include TV shows that are equal
                                 to, or have a higher average rating than this
                                 value. Expected value is a float.
        :param with_genres: (optional) Only include TV shows with the specified
                            genres. Expected value is an integer (the id of a
                            genre). Multiple values can be specified. Comma
                            separated indicates an 'AND' query, while a pipe (|)
                                separated value indicates an 'OR'.
        :param with_networks: (optional) Filter TV shows to include a specific
                              network. Expected value is an integer (the id of
                              a network). They can be comma separated to indicate
                              an 'AND' query.
        :param first_air_date.gte: (optional) The minimum air date to include.
                                   Expected format is YYYY-MM-DD.
        :param first_air_date.lte: (optional) The maximum air date to include.
                                   Expected format is YYYY-MM-DD.
        """
        path = self._get_path('tv')

        self._replace_underscore(kwargs)

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response
