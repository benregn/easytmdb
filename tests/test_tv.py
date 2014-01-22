# -*- coding: utf-8 -*-
import unittest

from easytmdb.tv import TV, TVSeasons, TVEpisodes, Networks


class TestTV(unittest.TestCase):
    def test_info(self):
        id = 1396
        name = 'Breaking Bad'
        tv = TV(id)
        tv.info()
        self.assertEqual(tv.name, name)

    def test_credits(self):
        id = 1396
        tv = TV(id)
        tv.credits()
        self.assertTrue(hasattr(tv, 'cast'))

    def test_external_ids(self):
        id = 1396
        imdb_id = 'tt0903747'
        tv = TV(id)
        tv.external_ids()
        self.assertEqual(tv.imdb_id, imdb_id)

    def test_images(self):
        id = 1396
        tv = TV(id)
        tv.images()
        self.assertTrue(hasattr(tv, 'backdrops'))

    def test_translations(self):
        id = 1396
        tv = TV(id)
        tv.translations()
        self.assertTrue(hasattr(tv, 'translations'))

    def test_top_rated(self):
        tv = TV()
        tv.top_rated()
        self.assertTrue(hasattr(tv, 'results'))

    def test_popular(self):
        tv = TV()
        tv.popular()
        self.assertTrue(hasattr(tv, 'results'))


class TestTVSeasons(unittest.TestCase):
    def test_info(self):
        id = 3572
        season_number = 1
        name = 'Season 1'
        tv_seasons = TVSeasons(id, season_number)
        tv_seasons.info()
        self.assertEqual(tv_seasons.name, name)

    def test_credits(self):
        id = 3572
        season_number = 1
        tv_seasons = TVSeasons(id, season_number)
        tv_seasons.credits()
        self.assertTrue(hasattr(tv_seasons, 'crew'))

    def test_external_ids(self):
        id = 3572
        season_number = 1
        tvdb_id = 2547
        tv_seasons = TVSeasons(id, season_number)
        tv_seasons.external_ids()
        self.assertEqual(tv_seasons.tvdb_id, tvdb_id)

    def test_images(self):
        id = 3572
        season_number = 1
        tv_seasons = TVSeasons(id, season_number)
        tv_seasons.images()
        self.assertTrue(hasattr(tv_seasons, 'posters'))


class TestTVEpisodes(unittest.TestCase):
    def test_info(self):
        id = 1396
        season_number = 1
        episode_number = 1
        name = 'Pilot'
        tv_episodes = TVEpisodes(id, season_number, episode_number)
        tv_episodes.info()
        self.assertEqual(tv_episodes.name, name)

    def test_credits(self):
        id = 1396
        season_number = 1
        episode_number = 1
        tv_episodes = TVEpisodes(id, season_number, episode_number)
        tv_episodes.credits()
        self.assertTrue(hasattr(tv_episodes, 'guest_stars'))

    def test_external_ids(self):
        id = 1396
        season_number = 1
        episode_number = 1
        imdb_id = 'tt0959621'
        tv_episodes = TVEpisodes(id, season_number, episode_number)
        tv_episodes.external_ids()
        self.assertEqual(tv_episodes.imdb_id, imdb_id)

    def test_images(self):
        id = 1396
        season_number = 1
        episode_number = 1
        tv_episodes = TVEpisodes(id, season_number, episode_number)
        tv_episodes.images()
        self.assertTrue(hasattr(tv_episodes, 'stills'))


class TestNetworks(unittest.TestCase):
    def test_info(self):
        id = 49
        name = 'HBO'
        network = Networks(id)
        network.info()
        self.assertEqual(network.name, name)
