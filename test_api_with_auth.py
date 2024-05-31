from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

class TestAPIWithAuth(unittest.TestCase):

    def setUp(self):
        self.url = 'https://jsonplaceholder.typicode.com/albums'
        self.client_id = 'tu_client_id'
        self.client_secret = 'tu_client_secret'
        self.auth_url = 'https://tu.authserver.com/oauth/token'
        self.expected_texts = [
            'quidem molestiae enim', 
            'sunt qui excepturi placeat culpa', 
            'omnis laborum odio', 
            'non esse culpa molestiae omnis sed optio', 
            'eaque aut omnis a'
        ]

    def get_token(self):
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url=self.auth_url, client_id=self.client_id, client_secret=self.client_secret)
        return token

    def test_get_albums_with_auth(self):
        token = self.get_token()
        headers = {'Authorization': f"Bearer {token['access_token']}"}
        response = requests.get(self.url, headers=headers)
        self.assertEqual(response.status_code, 200)
        albums = response.json()

        for i in range(5):
            self.assertEqual(albums[i]['title'], self.expected_texts[i])

if __name__ == '__main__':
    unittest.main()

