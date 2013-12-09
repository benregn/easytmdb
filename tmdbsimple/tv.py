# -*- coding: utf-8 -*-
from base import TMDB


class TV(TMDB):
    """Interact with The Movie Database TV endpoints

    See: http://docs.themoviedb.apiary.io/#tv
    """
    BASE_PATH = 'tv/'
    URLS = {
        'info': '{id}',
        'credits': '{id}/credits',
        'external_ids': '{id}/external_ids',
        'images': '{id}/images',
        'translations': '{id}/translations',
        'top_rated': 'top_rated',
        'popular': 'popular',
    }

    def __init__(self, id=0):
        super(TV, self).__init__()
        self.id = id

    def info(self, **kwargs):
        """Get the primary information about a TV series by id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Ftv%2F%7Bid%7D

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any TV method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('info')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def credits(self, **kwargs):
        """Get the cast & crew information about a TV series.

        Just like on the TMDB website, this information is pulled from the last
        season of the series.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Ftv%2F%7Bid%7D%2Fcredits

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any TV method names. E.g.
                                   'credits, images'
        """
        path = self._get_id_path('credits')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def external_ids(self, **kwargs):
        """Get the external ids for a TV series.

        E.g. IMDB, TVRage, Freebase.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Ftv%2F%7Bid%7D%2Fexternal_ids

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_id_path('external_ids')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(self, **kwargs):
        """Get the images (posters and backdrops) for a TV series.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Ftv%2F%7Bid%7D%2Fimages

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param include_image_language: (optional) Comma separated ISO 639-1 codes,
                                       e.g. 'en, es'.
        """
        path = self._get_id_path('images')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def translations(self, **kwargs):
        """Get the list of translations that exist for a TV series.

        These translations cascade down to the episode level.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Ftv%2F%7Bid%7D%2Ftranslations
        """
        path = self._get_id_path('translations')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def top_rated(self, **kwargs):
        """Get the list of top rated TV shows.

        By default, this list will only include TV shows that have 2 or more
        votes. This list refreshes every day.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Ftv%2Ftop_rated

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_id_path('top_rated')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def popular(self, **kwargs):
        """Get the list of popular TV shows.

        This list refreshes every day.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Ftv%2Fpopular

        :param page: (optional) Result page number, e.g. 3.
        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_id_path('popular')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response


class TVSeasons(TMDB):
    """Interact with The Movie Database TV season endpoints

    See: http://docs.themoviedb.apiary.io/#tvseasons
    """
    BASE_PATH = 'tv/{id}/season/'
    URLS = {
        'info': '{season}',
        'credits': '{season}/credits',
        'external_ids': '{season}/external_ids',
        'images': '{season}/images'
    }

    def __init__(self, id, season_number):
        super(TVSeasons, self).__init__()
        self.id = id
        self.season_number = season_number

    def _get_season_id_path(self, key):
        return self._get_path(key).format(id=self.id, season=self.season_number)

    def info(self, **kwargs):
        """Get the primary information about a TV season.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Ftv%2F%7Bid%7D%2Fseason%2F%7Bseason_number%7D

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = self._get_season_id_path('info')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def credits(self, **kwargs):
        """Get the cast & crew credits for a TV season.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Ftv%2F%7Bid%7D%2Fseason%2F%7Bseason_number%7D%2Fcredits
        """
        path = self._get_season_id_path('credits')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def external_ids(self, **kwargs):
        """Get the external ids for a TV season.

        E.g. IMDB, TVRage, Freebase.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Ftv%2F%7Bid%7D%2Fseason%2F%7Bseason_number%7D%2Fexternal_ids

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_season_id_path('external_ids')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(self, **kwargs):
        """Get the images (posters) for a TV season.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Ftv%2F%7Bid%7D%2Fseason%2F%7Bseason_number%7D%2Fimages

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param include_image_language: (optional) Comma separated ISO 639-1 codes,
                                       e.g. 'en, es'.
        """
        path = self._get_season_id_path('images')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response


class TVEpisodes(TMDB):
    """Interact with The Movie Database TV episode endpoints

    See: http://docs.themoviedb.apiary.io/#tvepisodes
    """
    BASE_PATH = 'tv/{id}/season/{season}/episode/'
    URLS = {
        'info': '{episode}',
        'credits': '{episode}/credits',
        'external_ids': '{episode}/external_ids',
        'images': '{episode}/images'
    }

    def __init__(self, id, season_number, episode_number):
        super(TVEpisodes, self).__init__()
        self.id = id
        self.season_number = season_number
        self.episode_number = episode_number

    def _get_episode_id_path(self, key):
        return self._get_path(key).format(id=self.id, season=self.season_number,
                                          episode=self.episode_number)

    # http://preview.tinyurl.com/get-tv-id-episode
    # optional parameter: language
    def info(self, **kwargs):
        """Get the basic movie information for a specific movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        :param append_to_response: (optional) Any Movies method names. E.g.
                                   'credits, images'
        """
        path = self._get_episode_id_path('info')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    # http://preview.tinyurl.com/get-tv-id-episode-credits
    # optional parameter: language
    def credits(self, **kwargs):
        """Get the basic movie information for a specific movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D
        """
        path = self._get_episode_id_path('credits')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    # http://tinyurl.com/get-tv-id-episode-external-ids
    # optional parameter: language
    def external_ids(self, **kwargs):
        """Get the basic movie information for a specific movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_episode_id_path('external_ids')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(self, **kwargs):
        """Get the basic movie information for a specific movie id.

        TMDB doc: http://docs.themoviedb.apiary.io/#get-%2F3%2Fmovie%2F%7Bid%7D

        :param language: (optional) ISO 639-1 code, e.g. 'de'. For a list of
                         639-1 codes, see http://en.wikipedia.org/wiki/ISO_639-1
        """
        path = self._get_episode_id_path('images')

        response = self._get(path, kwargs)
        self._set_attrs_to_values(response)
        return response
