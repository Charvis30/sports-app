import http.client
import json
from django.shortcuts import render


def basketball_data(request):
    # NBA games
    conn = http.client.HTTPSConnection("odds.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "odds.p.rapidapi.com"
    }
    conn.request("GET", "/v4/sports/basketball_nba/scores", headers=headers)
    res = conn.getresponse()
    data = res.read()
    games_data = json.loads(data.decode("utf-8"))

    # NBA odds
    conn = http.client.HTTPSConnection("odds.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "odds.p.rapidapi.com"
    }
    conn.request("GET", "/v4/sports/basketball_nba/odds?regions=us&oddsFormat=american&markets=spreads", headers=headers)
    res = conn.getresponse()
    data = res.read()
    odds_data = json.loads(data.decode("utf-8"))

    # Combine both contexts into one
    context = {
        'games_data': games_data,
        'odds_data': odds_data
    }
    
    return render(request, 'basketball.html', context)