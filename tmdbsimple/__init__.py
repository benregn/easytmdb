# -*- coding: utf-8 -*-
from .search import Search
from .discover import Discover
from .movies import Movies, Collections, Companies, Genres, Keywords, Reviews
from .conf_auth import Authentication, Configuration
from .changes import Changes
from .account import Account, Lists
from .people import People, Credits, Jobs
from .tv import TV, TVSeasons, TVEpisodes


API_KEY = None
VERSION = '3'
DEBUG_URL = None
