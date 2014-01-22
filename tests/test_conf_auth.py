# -*- coding: utf-8 -*-
import unittest

from easytmdb.conf_auth import Configuration, Authentication

from . import REQUEST_TOKEN


def skip(func):
    from nose import SkipTest

    def wrapper(x):
        raise SkipTest()
    wrapper.__name__ = func.__name__
    return wrapper


class TestConfiguration(unittest.TestCase):

    def test_info(self):
        change_keys = [
            'adult', 'also_known_as', 'alternative_titles',
            'biography', 'birthday', 'budget', 'cast', 'character_names',
            'crew', 'deathday', 'general', 'genres', 'homepage', 'images',
            'imdb_id', 'name', 'original_title', 'overview', 'plot_keywords',
            'production_companies', 'production_countries', 'releases',
            'revenue', 'runtime', 'spoken_languages', 'status', 'tagline',
            'title', 'trailers', 'translations'
        ]

        config = Configuration()
        config.info()
        self.assertEqual(config.change_keys, change_keys)
        self.assertTrue(hasattr(config, 'images'))


class TestAuthentication(unittest.TestCase):
    def test_token_new(self):
        success = True
        auth = Authentication()
        auth.token_new()
        self.assertEqual(auth.success, success)

    @skip
    def test_session_new(self):
        """This test is skipped by default. To include it, run: `nosetests --no-skip`
        This test method requires a valid, user authenticated token as
        genereated by token_new. This can be achived by following step 2
        on https://www.themoviedb.org/documentation/api/sessions.
        """
        success = True
        auth = Authentication()
        auth.session_new(request_token=REQUEST_TOKEN)
        self.assertEqual(auth.success, success)

    def test_guest_session_new(self):
        success = True
        auth = Authentication()
        auth.guest_session_new()
        self.assertEqual(auth.success, success)
