# -*- coding: utf-8 -*-
from base import TMDB


class Configuration(TMDB):
    """Configuration information

    See: http://docs.themoviedb.apiary.io/#configuration
    """

    URLS = {
        'configuration': 'configuration',
    }

    def info(self, **kwargs):
        """Get the system wide configuration information.

        Some elements of the API require some knowledge of this configuration
        data. The purpose of this is to try and keep the actual API responses as
        light as possible. It is recommended you store this data within your
        application and check for updates every so often.

        This method currently holds the data relevant to building image URLs as
        well as the change key map.

        To build an image URL, you will need 3 pieces of data. The base_url,
        size and file_path. Simply combine them all and you will have a fully
        qualified URL. Here’s an example URL::

            http://d3gtl9l2a4fn1j.cloudfront.net/t/p/w500/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fconfiguration
        """
        path = self._get_path('configuration')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response


class Authentication(TMDB):
    """Generate ids needed to access user accounts or use write methods.

    See more about sessions: https://www.themoviedb.org/documentation/api/sessions
    """

    BASE_PATH = 'authentication/'
    URLS = {
        'token_new': 'token/new',
        'session_new': 'session/new',
        'guest_session_new': 'guest_session/new',
    }

    def token_new(self, **kwargs):
        """Generate a valid request token for user based authentication.

        A request token is required in order to request a session id. You can
        generate any number of request tokens but they will expire after 60
        minutes. As soon as a valid session id has been created the token will
        be destroyed.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fauthentication%2Ftoken%2Fnew
        """
        path = self._get_path('token_new')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def session_new(self, request_token, **kwargs):
        """Generate a session id for user based authentication.

        A `valid session <https://www.themoviedb.org/documentation/api/sessions>`_
        id is required in order to use any of the write methods.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fauthentication%2Fsession%2Fnew

        :param request_token: The token generated from :py:func:token_new the
                              user to approve. The token needs to be approved
                              by the user before being used here.
        """
        path = self._get_path('session_new')
        kwargs.update({'request_token': request_token})

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def guest_session_new(self, **kwargs):
        """Generate a guest session id.

        A guest session can be used to rate movies without having a registered
        TMDb user account. You should only generate a single guest session per
        user (or device) as you will be able to attach the ratings to a TMDb
        user account in the future. There is also IP limits in place so you
        should always make sure it's the end user doing the guest session actions.

        If a guest session is not used for the first time within 24 hours, it
        will be automatically discarded.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fauthentication%2Fguest_session%2Fnew
        """
        path = self._get_path('guest_session_new')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response
