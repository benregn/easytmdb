# -*- coding: utf-8 -*-
import unittest

from tmdbsimple import base
from tmdbsimple.changes import Changes

from . import API_KEY


base.api_key = API_KEY


class TestChanges(unittest.TestCase):
    def test_movie(self):
        changes = Changes()
        changes.movie()
        self.assertTrue(hasattr(changes, 'results'))

    def test_person(self):
        change = Changes()
        change.movie()
        self.assertTrue(hasattr(change, 'results'))
