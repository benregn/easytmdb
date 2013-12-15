# -*- coding: utf-8 -*-
from base import TMDB


class People(TMDB):
    """Get information about people in Movies and TV Shows.

    See: http://docs.themoviedb.apiary.io/#people
    """
    BASE_PATH = 'person/'
    URLS = {
        'info': '{id}',
        'movie_credits': '{id}/movie_credits',
        'tv_credits': '{id}/tv_credits',
        'tv_credits': '{id}/tv_credits',
        'combined_credits': '{id}/combined_credits',
        'images': '{id}/images',
        'changes': '{id}/changes',
        'popular': 'popular',
        'latest': 'latest',
    }

    def __init__(self, id=0):
        super(People, self).__init__()
        self.id = id

    def info(self, **kwargs):
        """Get the general person information for a specific id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fperson%2F%7Bid%7D

        :param append_to_response: (optional) Any People method names. E.g.
                                   'combined_credits, images'
        """
        path = self._get_id_path('info')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def movie_credits(self, **kwargs):
        """Get the movie credits for a specific person id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fperson%2F%7Bid%7D%2Fmovie_credits

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any People method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('movie_credits')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def tv_credits(self, **kwargs):
        """Get the TV credits for a specific person id.

        To get the expanded details for each record, call the :py:meth:`Credits.info`
        method with the provided `credit_id`. This will provide details about
        which episode and/or season the credit is for.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fperson%2F%7Bid%7D%2Ftv_credits

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any People method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('tv_credits')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def combined_credits(self, **kwargs):
        """Get the combined (movie and TV) credits for a specific person id.

        To get the expanded details for each TV record, call the :py:meth:`Credits.info`
        method with the provided `credit_id`. This will provide details about
        which episode and/or season the credit is for.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fperson%2F%7Bid%7D%2Fcombined_credits

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any People method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('combined_credits')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(self):
        """Get the images for a specific person id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fperson%2F%7Bid%7D%2Fimages
        """
        path = self._get_id_path('images')
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response

    def changes(self, **kwargs):
        """Get the changes for a specific person id.

        Changes are grouped by key, and ordered by date in descending order. By
        default, only the last 24 hours of changes are returned. The maximum number
        of days that can be returned in a single request is 14. The language is
        present on fields that are translatable.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fperson%2F%7Bid%7D%2Fchanges

        :param start_date: (optional) A string in the format 'YYYY-MM-DD'
        :param end_date: (optional) Same as start_date
        """
        path = self._get_id_path('changes')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def popular(self, **kwargs):
        """Get the list of popular people on The Movie Database.

        This list refreshes every day. The maximum number of items this list will include is 100.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fperson%2Fpopular

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_path('popular')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def latest(self):
        """Get the latest person id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fperson%2Flatest

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_path('latest')
        response = self._get(path)
        self._set_attrs_to_values(response)
        return response


class Credits(TMDB):
    """Get full credit details about a person.

    See: http://docs.themoviedb.apiary.io/#credits
    """
    BASE_PATH = 'credit/'
    URLS = {
        'info': '{credit}',
    }

    def __init__(self, credit_id):
        super(Credits, self).__init__()
        self.credit_id = credit_id

    def _get_credit_id_path(self, key):
        return self._get_path(key).format(credit=self.credit_id)

    def info(self, **kwargs):
        """Get the detailed information about a particular credit record.

        This is currently only supported with the new credit model found in TV.
        These ids can be found from any TV credit response as well as the
        :py:meth:`.tv_credits` and :py:meth:`.combined_credits` methods for people.

        The episodes object returns a list of episodes and are generally going
        to be guest stars. The season array will return a list of season numbers.
        Season credits are credits that were marked with the "add to every season"
        option in the editing interface and are assumed to be "season regulars".

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fcredit%2F%7Bcredit_id%7D

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_credit_id_path('info')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response


class Jobs(TMDB):
    """Interact with the Jobs endpoint.

    See: http://docs.themoviedb.apiary.io/#jobs
    """
    BASE_PATH = 'job/'
    URLS = {
        'list': 'list',
    }

    def __init__(self):
        super(Jobs, self).__init__()
        pass

    def list(self, **kwargs):
        """Get a list of valid jobs.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fjob%2Flist
        """
        path = self._get_path('list')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response
