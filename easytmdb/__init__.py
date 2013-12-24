# -*- coding: utf-8 -*-
import os

from .search import Search
from .discover import Discover
from .movies import Movies, Collections, Companies, Genres, Keywords, Reviews
from .conf_auth import Authentication, Configuration
from .changes import Changes
from .account import Account, Lists
from .people import People, Credits, Jobs
from .tv import TV, TVSeasons, TVEpisodes


def _get_env_key(key):
    try:
        return os.environ[key]
    except KeyError:
        return None

API_KEY = _get_env_key('TMDB_API_KEY')
VERSION = '3'
DEBUG_URL = _get_env_key('TMDB_DEBUG_URL')
