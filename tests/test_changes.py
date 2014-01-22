# -*- coding: utf-8 -*-
import unittest

from easytmdb.changes import Changes


class TestChanges(unittest.TestCase):
    def test_movie(self):
        changes = Changes()
        changes.movies()
        self.assertTrue(hasattr(changes, 'results'))

    def test_person(self):
        change = Changes()
        change.movies()
        self.assertTrue(hasattr(change, 'results'))
