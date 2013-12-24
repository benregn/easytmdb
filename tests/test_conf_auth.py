# -*- coding: utf-8 -*-
import unittest

import tmdbsimple as tmdb
from tmdbsimple.conf_auth import Configuration, Authentication

from . import API_KEY, DEBUG_URL, REQUEST_TOKEN


tmdb.API_KEY = API_KEY
tmdb.DEBUG_URL = DEBUG_URL


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

    def test_session_new(self):
        """This test method requires a valid, user authenticated token as
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
