# -*- coding: utf-8 -*-
import unittest

from tmdbsimple import base
from tmdbsimple.search import Search

from . import API_KEY


base.api_key = API_KEY
base.debug_url = 'http://private-dc67-themoviedb.apiary.io'


class TestSearch(unittest.TestCase):
    def test_movies(self):
        query = 'Club'
        search = Search()
        search.movies(query)
        self.assertTrue(hasattr(search, 'results'))

    def test_collections(self):
        query = 'Avenger'
        search = Search()
        search.collections({'query': query})
        self.assertTrue(hasattr(search, 'results'))

    def test_tv(self):
        query = 'Breaking'
        search = Search()
        search.tv({'query': query})
        self.assertTrue(hasattr(search, 'results'))

    def test_persons(self):
        query = 'Brad Pitt'
        search = Search()
        search.persons({'query': query})
        self.assertTrue(hasattr(search, 'results'))

    def test_lists(self):
        query = 'Oscars'
        search = Search()
        search.lists({'query': query})
        self.assertTrue(hasattr(search, 'results'))

    def test_companies(self):
        query = 'Sony Pictures'
        search = Search()
        search.companies({'query': query})
        self.assertTrue(hasattr(search, 'results'))

    def test_keywords(self):
        query = 'fight'
        search = Search()
        search.keywords({'query': query})
        self.assertTrue(hasattr(search, 'results'))
