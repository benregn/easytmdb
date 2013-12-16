# -*- coding: utf-8 -*-
import unittest

from tmdbsimple import base
from tmdbsimple.account import Account, Lists

from . import (API_KEY, SESSION_ID, SUCCESS_CODE, UPDATE_CODE, DELETE_CODE,
               USERNAME, MOVIE_ID, MOVIE_TITLE)


base.api_key = API_KEY
base.debug_url = 'http://private-dc67-themoviedb.apiary.io'


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.acct = Account(SESSION_ID)
        self.acct.info()

    def test_info(self):
        self.assertEqual(self.acct.username, USERNAME)

    def test_lists(self):
        self.acct.lists()
        self.assertTrue(hasattr(self.acct, 'results'))

    def test_favorite_movies(self):
        kwargs = {'movie_id': MOVIE_ID, 'favorite': True}
        self.acct.favorite(**kwargs)

        self.acct.favorite_movies()
        self.assertEqual(self.acct.results[0]['title'], MOVIE_TITLE)

        kwargs.update({'favorite': False})
        self.acct.favorite(**kwargs)

    def test_favorite(self):
        kwargs = {'movie_id': MOVIE_ID, 'favorite': True}
        self.acct.favorite(**kwargs)

        try:
            self.assertEqual(self.acct.status_code, SUCCESS_CODE)
        except AssertionError:
            self.assertEqual(self.acct.status_code, UPDATE_CODE)

        kwargs['favorite'] = False
        self.acct.favorite(**kwargs)

    def test_rated_movies(self):
        kwargs = {'page': 1, 'sort_by': 'created_at'}
        self.acct.rated_movies(**kwargs)
        self.assertTrue(hasattr(self.acct, 'results'))

    def test_add_movie_watchlist(self):
        kwargs = {'movie_id': MOVIE_ID, 'watchlist': True}
        self.acct.add_movie_watchlist(**kwargs)

        try:
            self.assertEqual(self.acct.status_code, SUCCESS_CODE)
        except AssertionError:
            self.assertEqual(self.acct.status_code, UPDATE_CODE)

        kwargs['watchlist'] = False
        self.acct.add_movie_watchlist(**kwargs)

    def test_get_movie_watchlist(self):
        kwargs = {'movie_id': MOVIE_ID, 'watchlist': True}
        self.acct.add_movie_watchlist(**kwargs)

        self.acct.movie_watchlist()
        titles = [m['title'] for m in self.acct.results]
        self.assertIn(MOVIE_TITLE, titles)

        kwargs['watchlist'] = False
        self.acct.add_movie_watchlist(**kwargs)


class TestLists(unittest.TestCase):
    #
    # Add test "create list with language"
    #
    def test_info(self):
        id = '509ec17b19c2950a0600050d'
        created_by = 'Travis Bell'
        _list = Lists(id)
        _list.info()
        self.assertEqual(_list.created_by, created_by)

    def test_item_status(self):
        id = '509ec17b19c2950a0600050d'
        movie_id = 74643
        _list = Lists(id)
        _list.item_status({'movie_id': movie_id})
        self.assertTrue(hasattr(_list, 'item_present'))

    def test_create_list(self):
        _list = Lists(session_id=SESSION_ID)
        kwargs = {'name': 'My awesome list', 'description': 'No duplicates here'}
        _list.create_list(**kwargs)

        self.assertEqual(_list.status_code, SUCCESS_CODE)

        _list = Lists(_list.list_id, SESSION_ID)
        _list.delete_list()

    def test_create_list_with_language(self):
        _list = Lists(session_id=SESSION_ID)
        kwargs = {'name': 'My aweome list', 'description': '', 'language': 'en'}
        _list.create_list(**kwargs)

        self.assertEqual(_list.status_code, SUCCESS_CODE)

        _list = Lists(_list.list_id, SESSION_ID)
        _list.delete_list()

    def test_add_item(self):
        _list = Lists(session_id=SESSION_ID)
        kwargs = {'name': 'Test', 'description': ''}
        _list.create_list(**kwargs)
        list_id = _list.list_id

        _list = Lists(list_id, SESSION_ID)
        _list.add_item(media_id=550)

        self.assertEqual(_list.status_code, UPDATE_CODE)

        _list = Lists(list_id, SESSION_ID)
        _list.delete_list()

    def test_remove_item(self):
        _list = Lists(session_id=SESSION_ID)
        kwargs = {'name': 'Test', 'description': ''}
        _list.create_list(**kwargs)
        list_id = _list.list_id

        _list = Lists(list_id, SESSION_ID)
        _list.add_item(media_id=550)

        _list.remove_item(media_id=550)

        self.assertEqual(_list.status_code, DELETE_CODE)

        _list = Lists(list_id, SESSION_ID)
        _list.delete_list()

    def test_delete_list(self):
        _list = Lists(session_id=SESSION_ID)
        kwargs = {'name': 'Test', 'description': ''}
        _list.create_list(**kwargs)
        list_id = _list.list_id

        _list = Lists(list_id, SESSION_ID)
        _list.delete_list()

        self.assertEqual(_list.status_code, DELETE_CODE)
