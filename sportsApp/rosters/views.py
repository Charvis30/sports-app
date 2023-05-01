import http.client
import json
from django.shortcuts import render
import requests
from datetime import datetime


# Create your views here.


######### NBA #############
def nba_teams(request):
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeams?schedules=true&rosters=true", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))

    context = {'teams': data}
    return render(request, 'nbateams.html', context)

def get_nba_roster(team_abv):
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", f"/getNBATeamRoster?teamAbv={team_abv}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def get_nba_schedule(team_abv):
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", f"/getNBATeamSchedule?teamAbv={team_abv}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))


def nba_roster(request, team_abv):
    nba_roster = get_nba_roster(team_abv)
    nba_schedule = get_nba_schedule(team_abv)
    
    context = {"nba_roster": nba_roster,
               "nba_schedule": nba_schedule,

                }
    return render(request, f"nba-teams/{team_abv.lower()}.html", context)



######### MLB #############

def mlb_teams(request):
    conn = http.client.HTTPSConnection("tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com"
    }
    conn.request("GET", "/getMLBTeams", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))

    context = {'teams': data}
    return render(request, 'mlbteams.html', context)


def get_mlb_roster(team_abv):
    conn = http.client.HTTPSConnection("tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com"
    }
    conn.request("GET", f"/getMLBTeamRoster?teamAbv={team_abv}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def get_mlb_schedule(team_abv):
    conn = http.client.HTTPSConnection("tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com"
    }
    conn.request("GET", f"/getMLBTeamSchedule?teamAbv={team_abv}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def mlb_roster(request, team_abv):
    mlb_roster = get_mlb_roster(team_abv)
    mlb_schedule = get_mlb_schedule(team_abv)
    context = {"mlb_roster": mlb_roster,
               "mlb_schedule": mlb_schedule}
    
    return render(request, f"mlb-teams/{team_abv.lower()}MLB.html", context)




###########NFL################

def nfl_teams(request):
    conn = http.client.HTTPSConnection("tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
    }
    conn.request("GET", "/getNFLTeams?rosters=true&schedules=false", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))

    context = {'teams': data}
    return render(request, 'nflteams.html', context)

def get_nfl_roster(team_abv):
    conn = http.client.HTTPSConnection("tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
    }
    conn.request("GET", f"/getNFLTeamRoster?teamAbv={team_abv}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def get_nfl_schedule(team_abv):
    conn = http.client.HTTPSConnection("tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
    }
    conn.request("GET", f"/getNFLTeamSchedule?teamAbv={team_abv}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))


def nfl_roster(request, team_abv):
    nfl_roster = get_nfl_roster(team_abv)
    nfl_schedule = get_nfl_schedule(team_abv)
    context = {"nfl_roster": nfl_roster,
               "nfl_schedule": nfl_schedule}
    
    return render(request, f"nfl-teams/{team_abv.lower()}.html", context)



####NHL

def nhl_teams(request):
    conn = http.client.HTTPSConnection("nhl-stats-and-live-data.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "nhl-stats-and-live-data.p.rapidapi.com"
    }
    conn.request("GET", "/teams?season=20222023&expand=team.roster", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))

    context = {'teams': data}
    return render(request, 'nhlteams.html', context)

def get_nhl_roster(id):
    conn = http.client.HTTPSConnection("nhl-stats-and-live-data.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "nhl-stats-and-live-data.p.rapidapi.com"
    }
    conn.request("GET", f"/teams/{id}/roster", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def nhl_roster(request, id):
    nhl_roster = get_nhl_roster(id)
    context = {"nhl_roster": nhl_roster}
    return render(request, f"nhl-teams/{id}.html", context)

