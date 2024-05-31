import requests
import unittest

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.url = 'https://jsonplaceholder.typicode.com/albums'
        self.expected_texts = [
            'quidem molestiae enim', 
            'sunt qui excepturi placeat culpa', 
            'omnis laborum odio', 
            'non esse culpa molestiae omnis sed optio', 
            'eaque aut omnis a'
        ]

    def test_get_albums(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)
        albums = response.json()

        for i in range(5):
            self.assertEqual(albums[i]['title'], self.expected_texts[i])

if __name__ == '__main__':
    unittest.main()

