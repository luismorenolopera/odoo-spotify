from requests import request


class SpotifyTrackAPI(object):
    root_url = 'https://api.spotify.com/v1'
    recommendations_path = '/recommendations'

    def __init__(self, token, market):
        self._token = token
        self._market = market

    def get_title(self):
        try:
            title = self.track['name']
        except KeyError:
            return 'unknown'
        return title

    def get_artist(self):
        try:
            artist = self.track['artists'][0]['name']
        except (KeyError, IndexError):
            return 'unknown'
        return artist

    def get_track_url(self):
        try:
            title = self.track['external_urls']['spotify']
        except KeyError:
            return ''
        return title

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {token}'.format(token=self._token),
        }

    def get_recommendations(self, genres):
        response = request(
            'GET',
            url=self.get_recommendations_url(),
            headers=self.get_headers(),
            params=self.get_recommendations_url_params(genres),
        )
        self.track = response.json()['tracks'][0]

    def get_recommendations_url(self):
        return '{root_url}{recommendations_path}'.format(
            root_url=self.root_url,
            recommendations_path=self.recommendations_path,
        )

    def get_recommendations_url_params(self, genres, limit=1):
        return {
            'limit': str(limit),
            'market': self._market,
            'seed_genres': genres,
        }
