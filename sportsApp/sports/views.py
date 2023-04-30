import http.client
import json
from django.shortcuts import render
from django.utils import timezone


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

#Baseball
def baseball_data(request):
    # NBA games
    conn = http.client.HTTPSConnection("odds.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "odds.p.rapidapi.com"
    }
    conn.request("GET", "/v4/sports/baseball_mlb/scores", headers=headers)
    res = conn.getresponse()
    data = res.read()
    games_data = json.loads(data.decode("utf-8"))

    # MLB odds
    conn = http.client.HTTPSConnection("odds.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "odds.p.rapidapi.com"
    }
    conn.request("GET", "/v4/sports/baseball_mlb/odds?regions=us&oddsFormat=american&markets=spreads", headers=headers)
    res = conn.getresponse()
    data = res.read()
    odds_data = json.loads(data.decode("utf-8"))

    # Combine both contexts into one
    context = {
        'games_data': games_data,
        'odds_data': odds_data
    }
    
    return render(request, 'baseball.html', context)

#hockey
def hockey_data(request):
    # NBA games
    conn = http.client.HTTPSConnection("odds.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "odds.p.rapidapi.com"
    }
    conn.request("GET", "/v4/sports/icehockey_nhl/scores", headers=headers)
    res = conn.getresponse()
    data = res.read()
    games_data = json.loads(data.decode("utf-8"))

    # NHL odds
    conn = http.client.HTTPSConnection("odds.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "odds.p.rapidapi.com"
    }
    conn.request("GET", "/v4/sports/icehockey_nhl/odds?regions=us&oddsFormat=american&markets=spreads", headers=headers)
    res = conn.getresponse()
    data = res.read()
    odds_data = json.loads(data.decode("utf-8"))

    # Combine both contexts into one
    context = {
        'games_data': games_data,
        'odds_data': odds_data
    }
    
    return render(request, 'hockey.html', context)

#mls soccer
def soccer_data(request):
    # soccer games
    conn = http.client.HTTPSConnection("odds.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "odds.p.rapidapi.com"
    }
    conn.request("GET", "/v4/sports/soccer_usa_mls/scores", headers=headers)
    res = conn.getresponse()
    data = res.read()
    games_data = json.loads(data.decode("utf-8"))

    # MLS odds
    conn = http.client.HTTPSConnection("odds.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "odds.p.rapidapi.com"
    }
    conn.request("GET", "/v4/sports/soccer_usa_mls/odds?regions=us&oddsFormat=american&markets=spreads", headers=headers)
    res = conn.getresponse()
    data = res.read()
    odds_data = json.loads(data.decode("utf-8"))

    # Combine both contexts into one
    context = {
        'games_data': games_data,
        'odds_data': odds_data
    }
    
    return render(request, 'soccer.html', context)

#TIME
def format_commence_time(commence_time):
    dt = timezone.datetime.strptime(commence_time, '%Y-%m-%dT%H:%M:%SZ')
    formatted_time = dt.strftime('%-m/%-d %-I:%M%p')
    return formatted_time