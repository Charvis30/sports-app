from django.test import TestCase
from django.urls import reverse



# Create your tests here.
class BaseballDataTestCase(TestCase):
    def test_baseball_data(self):
        url = reverse('baseball')
        response = self.client.get(url)
        
        # Check if the response contains the expected data
        self.assertIn('games_data', response.context)
        self.assertIn('odds_data', response.context)
        self.assertTemplateUsed(response, 'baseball.html')


class BasketballDataTestCase(TestCase):
    """testing baseball data"""
    def test_baseball_data(self):
        """testing baseball data"""
        url = reverse('basketball')
        response = self.client.get(url)
        
        # Check if the response contains the expected data
        self.assertIn('games_data', response.context)
        self.assertIn('odds_data', response.context)
        self.assertTemplateUsed(response, 'basketball.html')


class HockeyDataTestCase(TestCase):
    """testing hockey data"""
    def test_hockey_data(self):
        """testing hockey data"""
        url = reverse('hockey')
        response = self.client.get(url)
        
        # Check if the response contains the expected data
        self.assertIn('games_data', response.context)
        self.assertIn('odds_data', response.context)
        self.assertTemplateUsed(response, 'hockey.html')

class SoccerDataTestCase(TestCase):
    def test_soccer_data(self):
        url = reverse('soccer')
        response = self.client.get(url)
        
        # Check if the response contains the expected data
        self.assertIn('games_data', response.context)
        self.assertIn('odds_data', response.context)
        self.assertTemplateUsed(response, 'soccer.html')


