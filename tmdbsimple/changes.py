# -*- coding: utf-8 -*-
from base import TMDB


class Changes(TMDB):
    """

    See: http://docs.themoviedb.apiary.io/#changes
    """
    BASE_PATH = ''
    URLS = {
        'movie': 'movie/changes',
        'person': 'person/changes',
    }

    def __init__(self):
        super(Changes, self).__init__()

    def movie(self, **kwargs):
        """Get a list of movie ids that have been edited.

        By default the last 24 hours are shown and only 100 items per page. The
        maximum number of days that can be returned in a single request is 14.
        You can then use the movie changes API to get the actual data that has
        been changed.

        **Please note**: The change log system to support this was changed on
        October 5, 2012 and will only show movies that have been edited since.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Fchanges

        :param page: (optional) Result page number, e.g. 3.
        :param start_date: (optional) A string in the format 'YYYY-MM-DD'.
        :param end_date: (optional) Same as start_date.
        """
        path = self._get_path('movie')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def person(self, **kwargs):
        """Get a list of person ids that have been edited.

        By default the last 24 hours are shown and only 100 items per page. The
        maximum number of days that can be returned in a single request is 14.
        You can then use the movie changes API to get the actual data that has
        been changed.

        **Please note**: The change log system to support this was changed on
        October 5, 2012 and will only show movies that have been edited since.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Fchanges

        :param page: (optional) Result page number, e.g. 3.
        :param start_date: (optional) A string in the format 'YYYY-MM-DD'.
        :param end_date: (optional) Same as start_date.
        """
        path = self._get_path('person')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response
