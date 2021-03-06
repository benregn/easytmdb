# -*- coding: utf-8 -*-
import unittest

from easytmdb.movies import Movies, Collections, Companies, Genres, Keywords, Reviews

from . import SESSION_ID, SUCCESS_CODE, UPDATE_CODE


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
        movie = Movies(id)
        movie.rating(rating=7.5, session_id=SESSION_ID)
        try:
            self.assertEqual(movie.status_code, SUCCESS_CODE)
        except AssertionError:
            self.assertEqual(movie.status_code, UPDATE_CODE)


class TestCollections(unittest.TestCase):
    def test_info(self):
        id = 10
        name = 'Star Wars Collection'
        collection = Collections(id)
        collection.info()
        self.assertEqual(collection.name, name)

    def test_images(self):
        id = 10
        collection = Collections(id)
        collection.images()
        self.assertTrue(hasattr(collection, 'backdrops'))


class TestCompanies(unittest.TestCase):
    def test_info(self):
        id = 1
        name = 'Lucasfilm'
        company = Companies(id)
        company.info()
        self.assertEqual(company.name, name)

    def test_movies(self):
        id = 1
        company = Companies(id)
        company.movies()
        self.assertTrue(hasattr(company, 'results'))


class TestGenres(unittest.TestCase):
    def test_list(self):
        genre = Genres()
        genre.list()
        self.assertTrue(hasattr(genre, 'genres'))

    def test_movies(self):
        id = 18
        genre = Genres(id)
        genre.movies()
        self.assertTrue(hasattr(genre, 'results'))


class TestKeywords(unittest.TestCase):
    def test_info(self):
        id = 1721
        name = 'fight'
        keyword = Keywords(id)
        keyword.info()
        self.assertEqual(keyword.name, name)

    def test_movies(self):
        id = 1721
        keyword = Keywords(id)
        keyword.movies()
        self.assertTrue(hasattr(keyword, 'results'))


class TestReviews(unittest.TestCase):
    def test_info(self):
        id = '5013bc76760ee372cb00253e'
        author = 'Chris'
        review = Reviews(id)
        review.info()
        self.assertEqual(review.author, author)
