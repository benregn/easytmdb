# -*- coding: utf-8 -*-
from base import TMDB


class Search(TMDB):
    """Search movies, TV shows, collections, persons, lists, companies and
    keywords.

    See: http://docs.themoviedb.apiary.io/#search
    """
    BASE_PATH = 'search/'
    URLS = {
        'movie': 'movie',
        'collection': 'collection',
        'tv': 'tv',
        'person': 'person',
        'list': 'list',
        'company': 'company',
        'keyword': 'keyword',
        'multi': 'multi',
    }

    def __init__(self):
        super(Search, self).__init__()

    def movies(self, query, **kwargs):
        """Search for movies by title.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fsearch%2Fmovie

        :param query: CGI escaped (URL encoded) string
        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param include_adult: (optional) Toggle the inclusion of adult titles.
                              Either `True` or `False`.
        :param year: (optional) Only include movies that have this year in their
                     release dates.
        :param primary_release_year: (optional) Only include movies that have
                                     have this year in their primary release
                                     dates.
        :param search_type: (optional) By default, the search type is 'phrase'.
                            This is almost guaranteed the option you will want.
                            It's a great all purpose search type and by far the
                            most tuned for every day querying. For those wanting
                            more of an "autocomplete" type search, set this
                            option to 'ngram'.
        """
        path = self._get_path('movie')
        kwargs.update({'query': query})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def collections(self, query, **kwargs):
        """Search for collections by name.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fsearch%2Fcollection

        :param query: CGI escaped (URL encoded) string
        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_path('collection')
        kwargs.update({'query': query})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def tv(self, query, **kwargs):
        """Search for TV shows by title.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fsearch%2Ftv

        :param query: CGI escaped (URL encoded) string
        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param first_air_date_year: (optional) Filter the results to only match
                                    shows that have a air date with with value.
        :param search_type: (optional) By default, the search type is 'phrase'.
                            This is almost guaranteed the option you will want.
                            It's a great all purpose search type and by far the
                            most tuned for every day querying. For those wanting
                            more of an "autocomplete" type search, set this
                            option to 'ngram'.
        """
        path = self._get_path('tv')
        kwargs.update({'query': query})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def persons(self, query, **kwargs):
        """Search for people by name.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fsearch%2Fperson

        :param query: CGI escaped (URL encoded) string
        :param page: (optional) Result page number, e.g. 3.
        :param include_adult: (optional) Toggle the inclusion of adult titles.
                              Either `True` or `False`.
        :param search_type: (optional) By default, the search type is 'phrase'.
                            This is almost guaranteed the option you will want.
                            It's a great all purpose search type and by far the
                            most tuned for every day querying. For those wanting
                            more of an "autocomplete" type search, set this
                            option to 'ngram'.
        """
        path = self._get_path('person')
        kwargs.update({'query': query})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def lists(self, query, **kwargs):
        """Search for lists by name and description.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fsearch%2Flist

        :param query: CGI escaped (URL encoded) string
        :param page: (optional) Result page number, e.g. 3.
        :param include_adult: (optional) Toggle the inclusion of adult titles.
                              Either `True` or `False`.
        """
        path = self._get_path('list')
        kwargs.update({'query': query})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def companies(self, query, **kwargs):
        """Search for companies by name.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fsearch%2Fcompany

        :param query: CGI escaped (URL encoded) string
        :param page: (optional) Result page number, e.g. 3.
        """
        path = self._get_path('company')
        kwargs.update({'query': query})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def keywords(self, query, **kwargs):
        """Search for keywords by name.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fsearch%2Fkeyword

        :param query: CGI escaped (URL encoded) string
        :param page: (optional) Result page number, e.g. 3.
        """
        path = self._get_path('keyword')
        kwargs.update({'query': query})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def multi(self, query, **kwargs):
        """Search the movie, tv show and person collections with a single query.

        Each item returned in the result array has a media_type field that maps to
        either movie, tv or person. Each mapped result is the same response you
        would get from each independent search.

        :param query: search string
        :param page: (optional) Result page number, e.g. 3.
        """
        path = self._get_path('multi')
        kwargs.update({'query': query})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response
