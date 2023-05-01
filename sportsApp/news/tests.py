from django.test import TestCase, Client
from unittest.mock import patch
from .views import news

nba_news_data = [
    {
        "title": "NBA News 1",
        "url": "https://nba.com/news1",
        "source": "NBA.com",
    },
    {
        "title": "NBA News 2",
        "url": "https://nba.com/news2",
        "source": "NBA.com",
    },
]

nfl_news_data = [
    {
        "title": "NFL News 1",
        "url": "https://nfl.com/news1",
        "source": "NFL.com",
    },
    {
        "title": "NFL News 2",
        "url": "https://nfl.com/news2",
        "source": "NFL.com",
    },
]

class NewsViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def mock_api_responses(self, nba_news_data, nfl_news_data):
        def mocked_request_get(*args, **kwargs):
            class MockResponse:
                def __init__(self, json_data, status_code):
                    self.json_data = json_data
                    self.status_code = status_code

                def json(self):
                    return self.json_data

            if args[0].startswith("https://nba-latest-news.p.rapidapi.com"):
                return MockResponse(nba_news_data, 200)
            elif args[0].startswith("https://football-news-live1.p.rapidapi.com"):
                return MockResponse(nfl_news_data, 200)

            return MockResponse(None, 404)

        return mocked_request_get

    @patch('requests.get')
    def test_news_view_renders_correct_template(self, mock_get):
        mock_get.side_effect = self.mock_api_responses(nba_news_data, nfl_news_data)
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')

    @patch('requests.get')
    def test_news_view_contains_all_leagues(self, mock_get):
        mock_get.side_effect = self.mock_api_responses(nba_news_data, nfl_news_data)
        response = self.client.get('/news/')
        self.assertIn('nba_news_data', response.context)
        self.assertIn('nfl_news_data', response.context)

    @patch('requests.get')
    def test_news_view_contains_news_data(self, mock_get):
        mock_get.side_effect = self.mock_api_responses(nba_news_data, nfl_news_data)
        response = self.client.get('/news/')

        nba_news_data_response = response.context['nba_news_data']
        nfl_news_data_response = response.context['nfl_news_data']

        self.assertTrue(len(nba_news_data_response) > 0, "NBA news data is empty.")
        self.assertTrue(len(nfl_news_data_response) > 0, "NFL news data is empty.")
