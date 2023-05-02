from django.test import TestCase
import http.client
import json
from django.test import TestCase, Client
from django.urls import reverse

class SportsAppTestCase(TestCase):

    def test_nba_teams_view(self):
        response = self.client.get(reverse('nba_teams'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nbateams.html')

    def test_mlb_teams_view(self):
        response = self.client.get(reverse('mlb_teams'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mlbteams.html')

    def test_nfl_teams_view(self):
        response = self.client.get(reverse('nfl_teams'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nflteams.html')

    def test_nhl_teams_view(self):
        response = self.client.get(reverse('nhl_teams'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nhlteams.html')

    def test_nba_roster_view(self):
        response = self.client.get(reverse('nba_roster', args=['LAL']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nba-teams/lal.html')

    def test_mlb_roster_view(self):
        response = self.client.get(reverse('mlb_roster', args=['TOR']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mlb-teams/torMLB.html')

    def test_nfl_roster_view(self):
        response = self.client.get(reverse('nfl_roster', args=['DAL']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nfl-teams/dal.html')

    def test_nhl_roster_view(self):
        response = self.client.get(reverse('nhl_roster', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nhl-teams/1.html')

    def test_nba_teams_data(self):
        conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
            'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
        }
        conn.request("GET", "/getNBATeams?schedules=true&rosters=true", headers=headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data.decode("utf-8"))
        self.assertTrue(len(data) > 0)

    def test_mlb_teams_data(self):
        conn = http.client.HTTPSConnection("tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
            'X-RapidAPI-Host': "tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com"
        }
        conn.request("GET", "/getMLBTeams", headers=headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data.decode("utf-8"))
        self.assertTrue(len(data) > 0)

    def test_nfl_teams_data(self):
        conn = http.client.HTTPSConnection("tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
            'X-RapidAPI-Host': "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }
        conn.request("GET", "/getNFLTeams?rosters=true&schedules=false", headers=headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data.decode("utf-8"))
        self.assertIsInstance(data, list)
