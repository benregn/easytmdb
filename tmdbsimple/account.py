# -*- coding: utf-8 -*-
from base import TMDB


class Account(TMDB):
    """Interact with a The Movie Database user account.

    See: http://docs.themoviedb.apiary.io/#account
    """
    BASE_PATH = 'account/'
    URLS = {
        'lists': '{account}/lists',
        'favorite_movies': '{account}/favorite_movies',
        'favorite': '{account}/favorite',
        'rated_movies': '{account}/rated_movies',
        'movie_watchlist': '{account}/movie_watchlist',
    }

    def __init__(self, session_id):
        super(Account, self).__init__()
        self.session_id = session_id

    def _get_account_id_path(self, key):
        return self._get_path(key).format(account=self.account_id)

    def info(self, **kwargs):
        """Get the basic information for an account.

        This method has to be called before calling any other Account methods.

        You will need to have a `valid session <https://www.themoviedb.org/documentation/api/sessions>`_ id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Faccount
        """
        path = self.BASE_PATH[:-1]
        kwargs.update({'session_id': self.session_id})

        response = self._get(path, kwargs)
        # about account_id: http://www.themoviedb.org/talk/527f91b4760ee361f707cf57
        self.account_id = response['id']
        self._set_attrs_to_values(response)
        return response

    def lists(self, **kwargs):
        """Get the lists that you have created and marked as a favorite.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Faccount%2F%7Bid%7D%2Flists

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_account_id_path('lists')
        kwargs.update({'session_id': self.session_id})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def favorite_movies(self, **kwargs):
        """Get the list of favorite movies for an account.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Faccount%2F%7Bid%7D%2Ffavorite_movies

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param sort_by: (optional) Only 'created_at` is currently supported.
        :param sort_order: (optional) Either 'asc' or 'desc'.
        """
        path = self._get_account_id_path('favorite_movies')
        kwargs.update({'session_id': self.session_id})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def favorite(self, movie_id, favorite, **kwargs):
        """Add or remove a movie to an accounts favorite list.

        TMDB doc: http://docs.themoviedb.apiary.io/#post-%2F3%2Faccount%2F%7Bid%7D%2Ffavorite

        :param movie_id: The id of the movie to favorite or unfavorite.
        :param favorite: Either `True` to favorite `movie_id` or `False` to
                         unfavorite.
        """
        path = self._get_account_id_path('favorite')
        kwargs.update({'session_id': self.session_id})
        payload = {'movie_id': movie_id, 'favorite': favorite}

        response = self._post(path, kwargs, payload)
        self._set_attrs_to_values(response)
        return response

    def rated_movies(self, **kwargs):
        """Get the list of rated movies (and associated rating) for an account.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Faccount%2F%7Bid%7D%2Frated_movies

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param sort_by: (optional) Only 'created_at` is currently supported.
        :param sort_order: (optional) Either 'asc' or 'desc'.
        """
        path = self._get_account_id_path('rated_movies')
        kwargs.update({'session_id': self.session_id})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def get_movie_watchlist(self, **kwargs):
        """Get the list of movies on an accounts watchlist.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Faccount%2F%7Bid%7D%2Fmovie_watchlist

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param sort_by: (optional) Only 'created_at` is currently supported.
        :param sort_order: (optional) Either 'asc' or 'desc'.
        """
        path = self._get_account_id_path('movie_watchlist')
        kwargs.update({'session_id': self.session_id})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def add_movie_watchlist(self, movie_id, watchlist, **kwargs):
        """Add or remove a movie to an accounts watch list.

        TMDB doc: http://docs.themoviedb.apiary.io/#post-%2F3%2Faccount%2F%7Bid%7D%2Ffavorite_movies

        :param movie_id: The id of the movie to add or remove from watchlist.
        :param watchlist: Either `True` to add `movie_id` to watchlist or
                          `False` to remove.
        """
        path = self._get_account_id_path('movie_watchlist')
        kwargs.update({'session_id': self.session_id})
        payload = {'movie_id': movie_id, 'movie_watchlist': watchlist}

        response = self._post(path, kwargs, payload)
        self._set_attrs_to_values(response)
        return response


class Lists(TMDB):
    """Get lists and interact with lists.

    See: http://docs.themoviedb.apiary.io/#lists
    """
    BASE_PATH = 'list/'
    URLS = {
        'info': '{id}',
        'item_status': '{id}/item_status',
        'add_item': '{id}/add_item',
        'remove_item': '{id}/remove_item',
        'delete_list': '{id}',
    }

    def __init__(self, id=0, session_id=0):
        super(Lists, self).__init__()
        self.id = id
        self.session_id = session_id

    def info(self, **kwargs):
        """Get a list by id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Flist%2F%7Bid%7D
        """
        path = self._get_id_path('info')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def item_status(self, movie_id, **kwargs):
        """Check to see if a movie ID is already added to a list.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Flist%2F%7Bid%7D%2Fitem_status

        :param language: Check to see if this movie ID is already part of a
                         list or not.
        """
        path = self._get_id_path('item_status')
        kwargs.update({'movie_id': movie_id})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def create_list(self, name, description, **kwargs):
        """Create a new list.

        A `valid session <https://www.themoviedb.org/documentation/api/sessions>`_
        id is required.

        TMDB doc: http://docs.themoviedb.apiary.io/#post-%2F3%2Flist

        :param name: The name of the list to create.
        :param description: A description of the list.
        :param language: (optional) Probably a ISO 639-1 code (Waiting on confirmation from TMDB).
        """
        path = self.BASE_PATH[:-1]
        kwargs.update({'session_id': self.session_id})
        payload = {'name': name, 'description': description}
        if 'language' in kwargs:
            payload.update({'language': kwargs.pop('language')})

        response = self._post(path, kwargs, payload)
        self._set_attrs_to_values(response)
        return response

    def add_item(self, media_id, **kwargs):
        """Add a new movie to a list that the user created.

        A `valid session <https://www.themoviedb.org/documentation/api/sessions>`_
        id is required.

        TMDB doc: http://docs.themoviedb.apiary.io/#post-%2F3%2Flist%2F%7Bid%7D%2Fadd_item

        :param media_id: The id of the item to add.
        """
        path = self._get_id_path('add_item')
        kwargs.update({'session_id': self.session_id})
        payload = {'media_id': media_id}

        response = self._post(path, kwargs, payload)
        self._set_attrs_to_values(response)
        return response

    def remove_item(self, media_id, **kwargs):
        """Delete a movie from a list that the user created.

        A `valid session <https://www.themoviedb.org/documentation/api/sessions>`_
        id is required.

        TMDB doc: http://docs.themoviedb.apiary.io/#post-%2F3%2Flist%2F%7Bid%7D%2Fremove_item

        :param media_id: The id of the item to remove.
        """
        path = self._get_id_path('remove_item')
        kwargs.update({'session_id': self.session_id})
        payload = {'media_id': media_id}

        response = self._post(path, kwargs, payload)
        self._set_attrs_to_values(response)
        return response

    def delete_list(self, **kwargs):
        """Delete a list that the user created.

        A `valid session <https://www.themoviedb.org/documentation/api/sessions>`_
        id is required.

        TMDB doc: http://docs.themoviedb.apiary.io/#delete-%2F3%2Flist%2F%7Bid%7D
        """
        path = self._get_id_path('delete_list')
        kwargs.update({'session_id': self.session_id})

        response = self._delete(path, kwargs)
        self._set_attrs_to_values(response)
        return response
