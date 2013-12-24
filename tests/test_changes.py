# -*- coding: utf-8 -*-
import unittest

import tmdbsimple as tmdb
from tmdbsimple.changes import Changes

from . import API_KEY, DEBUG_URL


tmdb.API_KEY = API_KEY
tmdb.DEBUG_URL = DEBUG_URL


class TestChanges(unittest.TestCase):
    def test_movie(self):
        changes = Changes()
        changes.movie()
        self.assertTrue(hasattr(changes, 'results'))

    def test_person(self):
        change = Changes()
        change.movie()
        self.assertTrue(hasattr(change, 'results'))
