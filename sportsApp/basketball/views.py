
import http.client
import json
from django.shortcuts import render


def basketball_data(request):
    conn = http.client.HTTPSConnection("free-nba.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "free-nba.p.rapidapi.com",
        'x-rapidapi-key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21"
        }
    conn.request("GET", "/teams?page=0", headers=headers)
    res = conn.getresponse()
    data = res.read()
    team_data = json.loads(data.decode("utf-8"))['data']
    context = {'api_data': data}

    # East and West conferences
    east_teams = []
    west_teams = []
    for team in team_data:
        if team['conference'] == 'East':
            east_teams.append(team)
        elif team['conference'] == 'West':
            west_teams.append(team)

    # Pass the lists as separate contexts to the HTML template
    context = {
        'east_teams': east_teams,
        'west_teams': west_teams
    }
    return render(request, 'basketball.html', context)


# Games 

def get_games_data(request):
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }

    conn.request("GET", "/getNBAGamesForDate?gameDate=20221202", headers=headers)

    res = conn.getresponse()
    data = res.read()

    games_data = json.loads(data.decode("utf-8"))

    context = {'games_data': games_data}

    return render(request, 'basketball.html', context)

