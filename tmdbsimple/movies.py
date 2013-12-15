# -*- coding: utf-8 -*-
from base import TMDB


class Movies(TMDB):
    """Interact with The Movie Database Movies endpoints

    See: http://docs.themoviedb.apiary.io/#movies
    """
    BASE_PATH = 'movie/'
    URLS = {
        'info': '{id}',
        'alternative_titles': '{id}/alternative_titles',
        'credits': '{id}/credits',
        'images': '{id}/images',
        'keywords': '{id}/keywords',
        'releases': '{id}/releases',
        'trailers': '{id}/trailers',
        'translations': '{id}/translations',
        'similar_movies': '{id}/similar_movies',
        'reviews': '{id}/reviews',
        'lists': '{id}/lists',
        'changes': '{id}/changes',
        'latest': 'latest',
        'upcoming': 'upcoming',
        'now_playing': 'now_playing',
        'popular': 'popular',
        'top_rated': 'top_rated',
        'account_states': '{id}/account_states',
        'rating': '{id}/rating',
    }

    def __init__(self, id=0):
        super(Movies, self).__init__()
        self.id = id

    def info(self, **kwargs):
        """Get the basic movie information for a specific movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('info')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def alternative_titles(self, **kwargs):
        """Get the alternative titles for a specific movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Falternative_titles

        :param country: (optional) ISO 3166-1 code, e.g. 'us'. For a list of
                        3166-1 codes, see http://en.wikipedia.org/wiki/ISO_3166-1
        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('alternative_titles')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def credits(self, **kwargs):
        """Get the cast and crew information for a specific movie id.

        TMDB docs: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fcredits

        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('credits')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(self, **kwargs):
        """Get the images (posters and backdrops) for a specific movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fimages

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param include_image_language: (optional) Comma separated ISO 639-1 codes,
                                       e.g. 'en, es'.
        :param append_to_response: (optional) Any Movies method names, comma
                                   separated, e.g. 'credits, images'.
        """
        path = self._get_id_path('images')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def keywords(self, **kwargs):
        """Get the plot keywords for a specific movie id.

        TMDB docs: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fkeywords

        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('keywords')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def releases(self, **kwargs):
        """Get the release date by country for a specific movie id.

        TMDB docs: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Freleases

        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('releases')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def trailers(self, **kwargs):
        """Get the trailers for a specific movie id.

        TMDB docs: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Ftrailers

        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('trailers')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def translations(self, **kwargs):
        """Get the translations for a specific movie id.

        TMDB docs: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Ftranslations

        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('translations')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def similar_movies(self, **kwargs):
        """Get the similar movies for a specific movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fsimilar_movies

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('similar_movies')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def reviews(self, **kwargs):
        """Get the reviews for a particular movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Freviews

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('reviews')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def lists(self, **kwargs):
        """Get the lists that the movie belongs to.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Flists

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('lists')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def changes(self, **kwargs):
        """Get the changes for a specific movie id.

        Changes are grouped by key, and ordered by date in descending order. By
        default, only the last 24 hours of changes are returned. The maximum number
        of days that can be returned in a single request is 14. The language is
        present on fields that are translatable.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Fchanges

        :param start_date: (optional) A string in the format 'YYYY-MM-DD'
        :param end_date: (optional) Same as start_date
        """
        path = self._get_id_path('changes')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def latest(self, **kwargs):
        """Get the latest movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Flatest
        """
        path = self._get_path('latest')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def upcoming(self, **kwargs):
        """Get the list of upcoming movies.

        This list refreshes every day. The maximum number of items this list will include is 100.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Fupcoming

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_path('upcoming')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def now_playing(self, **kwargs):
        """Get the list of movies playing in theatres.

        This list refreshes every day. The maximum number of items this list will include is 100.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Fnow_playing

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_path('now_playing')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def popular(self, **kwargs):
        """Get the list of popular movies on The Movie Database.

        This list refreshes every day.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Fpopular

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_path('popular')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def top_rated(self, **kwargs):
        """Get the list of top rated movies.

        This list refreshes every day. This list only includes movies that have
        10 or more votes.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2Ftop_rated

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_path('top_rated')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def account_states(self, session_id, **kwargs):
        """Get status of whether or not the movie has been rated or added to favourite or watch lists.

        A `valid session <https://www.themoviedb.org/documentation/api/sessions>`_ id is required.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Faccount_states

        :param session_id: A session id as returned from :py:meth:`.session_new`
        """
        path = self._get_id_path('account_states')
        kwargs.update({'session_id': session_id})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def rating(self, rating, session_id=None, guest_session_id=None, **kwargs):
        """Rate a movie.

        A `valid session <https://www.themoviedb.org/documentation/api/sessions>`_
        id or guest session id is required.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D%2Flists

        :param rating: A float
        :param session_id: A session id as returned from :py:meth:`.session_new`.
                           Required if guest_session_id is not specified.
        :param guest_session_id: A session id as returned from :py:meth:`.guest_session_new`
                                 Required if session_id is not specified.
        """
        path = self._get_id_path('rating')
        if session_id is None and guest_session_id is None:
            raise ValueError("Either 'session_id' or 'guest_session_id' keyword argument is required")
        kwargs.update({'value': rating})
        if session_id:
            kwargs.update({'session_id': session_id})
        else:
            kwargs.update({'guest_session_id': guest_session_id})

        response = self._post(path, kwargs)
        self._set_attrs_to_values(response)
        return response


class Collections(TMDB):
    """Get information about movie collections

    See: http://docs.themoviedb.apiary.io/#collections
    """
    BASE_PATH = 'collection/'
    URLS = {
        'info': '{id}',
        'images': '{id}/images',
    }

    def __init__(self, id):
        super(Collections, self).__init__()
        self.id = id

    def info(self, **kwargs):
        """Get the basic collection information for a specific collection id.

        You can get the ID needed for this method by making a :py:meth:`Movies.info`
        request and paying attention to the `belongs_to_collection` hash.

        Movie parts are not sorted in any particular order. If you would like
        to sort them yourself you can use the provided `release_date`.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fcollection%2F%7Bid%7D

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any Collections method names. E.g.
                                   'images'
        """
        path = self._get_id_path('info')
        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(self, **kwargs):
        """Get all of the images for a particular collection by collection id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fcollection%2F%7Bid%7D%2Fimages

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param include_image_language: (optional) Comma separated ISO 639-1 codes,
                                       e.g. 'en, es'.
        :param append_to_response: (optional) Any Movies method names, comma
                                   separated, e.g. 'credits, images'.
        """
        path = self._get_id_path('images')
        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response


class Companies(TMDB):
    """Get information about movie companies.

    See: http://docs.themoviedb.apiary.io/#companies
    """
    BASE_PATH = 'company/'
    URLS = {
        'info': '{id}',
        'movies': '{id}/movies',
    }

    def __init__(self, id=0):
        super(Companies, self).__init__()
        self.id = id

    def info(self, **kwargs):
        """Get the basic information about a movie company.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fcompany%2F%7Bid%7D

        :param append_to_response: (optional) Any Collections method names. E.g.
                                   'movies'
        """
        path = self._get_id_path('info')
        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def movies(self, **kwargs):
        """Get the list of movies associated with a particular company.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fcompany%2F%7Bid%7D%2Fmovies

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any Collections method names. E.g.
                                   'info'
        """
        path = self._get_id_path('movies')
        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response
