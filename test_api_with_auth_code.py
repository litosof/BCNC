from requests_oauthlib import OAuth2Session

class TestAPIWithAuthCode(unittest.TestCase):

    def setUp(self):
        self.url = 'https://jsonplaceholder.typicode.com/albums'
        self.client_id = 'tu_client_id'
        self.client_secret = 'tu_client_secret'
        self.auth_url = 'https://tu.authserver.com/oauth/authorize'
        self.token_url = 'https://tu.authserver.com/oauth/token'
        self.redirect_uri = 'https://tu.redirecturi.com/callback'
        self.scope = ['scope1', 'scope2']
        self.expected_texts = [
            'quidem molestiae enim', 
            'sunt qui excepturi placeat culpa', 
            'omnis laborum odio', 
            'non esse culpa molestiae omnis sed optio', 
            'eaque aut omnis a'
        ]

    def get_token(self):
        oauth = OAuth2Session(self.client_id, redirect_uri=self.redirect_uri, scope=self.scope)
        authorization_url, state = oauth.authorization_url(self.auth_url)

        print('Por favor abre el siguiente enlace en tu navegador e ingresa el código de autorización:')
        print(authorization_url)

        authorization_response = input('Introduce la URL completa de redirección después de la autorización: ')
        token = oauth.fetch_token(self.token_url, authorization_response=authorization_response, client_secret=self.client_secret)
        return token

    def test_get_albums_with_auth_code(self):
        token = self.get_token()
        headers = {'Authorization': f"Bearer {token['access_token']}"}
        response = requests.get(self.url, headers=headers)
        self.assertEqual(response.status_code, 200)
        albums = response.json()

        for i in range(5):
            self.assertEqual(albums[i]['title'], self.expected_texts[i])

if __name__ == '__main__':
    unittest.main()

