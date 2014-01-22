# -*- coding: utf-8 -*-
import unittest

from easytmdb.discover import Discover


class TestDiscover(unittest.TestCase):
    def test_movie(self):
        discover = Discover()
        discover.movie(page=1, year=2004)
        self.assertTrue(hasattr(discover, 'results'))

    def test_tv(self):
        discover = Discover()
        discover.tv(page=2, vote_average_gte=5)
        self.assertTrue(hasattr(discover, 'results'))
