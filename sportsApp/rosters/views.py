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
    game_date_str = "20230326"
    game_date = datetime.strptime(game_date_str, "%Y%m%d")
    context = {"nba_roster": nba_roster,
               "nba_schedule": nba_schedule,
               "game_date": game_date}
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


def get_team_roster(team_abv):
    conn = http.client.HTTPSConnection("tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com"
    }
    conn.request("GET", f"/getMLBTeamRoster?teamAbv={team_abv}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def dbacks_roster(request):
    team_roster = get_team_roster("ARI")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/diamondbacks.html", context)

def braves_roster(request):
    team_roster = get_team_roster("ATL")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/braves.html", context)

def orioles_roster(request):
    team_roster = get_team_roster("BAL")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/orioles.html", context)

def red_sox_roster(request):
    team_roster = get_team_roster("BOS")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/red_sox.html", context)

def cubs_roster(request):
    team_roster = get_team_roster("CHC")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/cubs.html", context)

def white_sox_roster(request):
    team_roster = get_team_roster("CHW")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/white_sox.html", context)

def reds_roster(request):
    team_roster = get_team_roster("CIN")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/reds.html", context)

def rockies_roster(request):
    team_roster = get_team_roster("COL")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/rockies.html", context)

def tigers_roster(request):
    team_roster = get_team_roster("DET")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/tigers.html", context)

def astros_roster(request):
    team_roster = get_team_roster("HOU")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/astros.html", context)

def royals_roster(request):
    team_roster = get_team_roster("KC")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/royals.html", context)

def angels_roster(request):
    team_roster = get_team_roster("LAA")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/angels.html", context)

def dodgers_roster(request):
    team_roster = get_team_roster("LAD")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/dodgers.html", context)

def marlins_roster(request):
    team_roster = get_team_roster("MIA")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/marlins.html", context)

def brewers_roster(request):
    team_roster = get_team_roster("MIL")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/brewers.html", context)

def twins_roster(request):
    team_roster = get_team_roster("MIN")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/twins.html", context)

def mets_roster(request):
    team_roster = get_team_roster("NYM")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/mets.html", context)

def yankees_roster(request):
    team_roster = get_team_roster("NYY")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/yankees.html", context)

def athletics_roster(request):
    team_roster = get_team_roster("OAK")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/athletics.html", context)

def phillies_roster(request):
    team_roster = get_team_roster("PHI")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/phillies.html", context)

def pirates_roster(request):
    team_roster = get_team_roster("PIT")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/pirates.html", context)

def padres_roster(request):
    team_roster = get_team_roster("SD")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/padres.html", context)

def giants_roster(request):
    team_roster = get_team_roster("SF")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/giants.html", context)

def mariners_roster(request):
    team_roster = get_team_roster("SEA")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/mariners.html", context)

def cardinals_roster(request):
    team_roster = get_team_roster("STL")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/cardinals.html", context)

def rays_roster(request):
    team_roster = get_team_roster("TB")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/rays.html", context)

def blue_jays_roster(request):
    team_roster = get_team_roster("TOR")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/bluejays.html", context)

def nationals_roster(request):
    team_roster = get_team_roster("WAS")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/nationals.html", context)

def rangers_roster(request):
    team_roster = get_team_roster("TEX")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/rangers.html", context)

def guardians_roster(request):
    team_roster = get_team_roster("CLE")
    context = {"team_roster": team_roster}
    return render(request, "mlb-teams/guardians.html", context)


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


def nfl_roster(request, team_abv):
    nfl_roster = get_nfl_roster(team_abv)
    context = {"nfl_roster": nfl_roster}
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

