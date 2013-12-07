# -*- coding: utf-8 -*-
import unittest

from tmdbsimple import tmdbsimple
from tmdbsimple.tmdbsimple import Movies

from . import API_KEY, SESSION_ID


tmdbsimple.api_key = API_KEY


class TestMovies(unittest.TestCase):
    def test_info(self):
        id = 103332
        title = 'Ruby Sparks'
        movie = Movies(id)
        movie.info()
        self.assertEqual(movie.title, title)

    def test_info_with_language(self):
        id = 103332
        title = "Elle s'appelle Ruby"
        movie = Movies(id)
        movie.info(language='fr')
        self.assertEqual(movie.title, title)

    def test_alternative_titles(self):
        id = 550
        movie = Movies(id)
        movie.alternative_titles()
        self.assertTrue(hasattr(movie, 'titles'))

    def test_credits(self):
        id = 103332
        movie = Movies(id)
        movie.credits()
        self.assertTrue(hasattr(movie, 'cast'))

    def test_images(self):
        id = 103332
        movie = Movies(id)
        movie.images()
        self.assertTrue(hasattr(movie, 'backdrops'))
        self.assertTrue(hasattr(movie, 'posters'))

    def test_keywords(self):
        id = 103332
        movie = Movies(id)
        movie.keywords()
        self.assertTrue(hasattr(movie, 'keywords'))

    def test_releases(self):
        id = 103332
        movie = Movies(id)
        movie.releases()
        self.assertTrue(hasattr(movie, 'countries'))

    def test_trailers(self):
        id = 103332
        movie = Movies(id)
        movie.trailers()
        self.assertTrue(hasattr(movie, 'youtube'))

    def test_translations(self):
        id = 550
        movie = Movies(id)
        movie.translations()
        self.assertTrue(hasattr(movie, 'translations'))

    def test_similar_movies(self):
        id = 550
        movie = Movies(id)
        movie.similar_movies()
        self.assertTrue(hasattr(movie, 'results'))

    def test_reviews(self):
        id = 49026
        movie = Movies(id)
        movie.reviews()
        self.assertTrue(hasattr(movie, 'results'))

    def test_lists(self):
        id = 103332
        movie = Movies(id)
        movie.lists()
        self.assertTrue(hasattr(movie, 'results'))

    def test_changes(self):
        id = 103332
        movie = Movies(id)
        movie.changes()
        self.assertTrue(hasattr(movie, 'changes'))

    def test_latest(self):
        movie = Movies()
        movie.latest()
        self.assertTrue(hasattr(movie, 'popularity'))

    def test_upcoming(self):
        movie = Movies()
        movie.upcoming()
        self.assertTrue(hasattr(movie, 'results'))

    def test_now_playing(self):
        movie = Movies()
        movie.now_playing()
        self.assertTrue(hasattr(movie, 'results'))

    def test_popular(self):
        movie = Movies()
        movie.popular()
        self.assertTrue(hasattr(movie, 'results'))

    def test_top_rated(self):
        movie = Movies()
        movie.top_rated()
        self.assertTrue(hasattr(movie, 'results'))

    def test_account_states(self):
        id = 550
        movie = Movies(id)
        movie.account_states(session_id=SESSION_ID)
        self.assertTrue(hasattr(movie, 'favorite'))

    def test_rating(self):
        id = 103332
        success_code = 1
        update_code = 12
        movie = Movies(id)
        movie.rating(rating=7.5, session_id=SESSION_ID)
        try:
            self.assertEqual(movie.status_code, success_code)
        except AssertionError:
            self.assertEqual(movie.status_code, update_code)
