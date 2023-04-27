import http.client
import json
from django.shortcuts import render
import requests

# Create your views here.

######### NBA #############
def nba_teams(request):
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeams?schedules=false&rosters=true", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))

    context = {'teams': data}
    return render(request, 'nbateams.html', context)



def boston_roster(request):
    # Boston Celtics
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=BOS", headers=headers)
    res = conn.getresponse()
    data = res.read()
    boston_roster = json.loads(data.decode("utf-8"))

    context = {'boston_roster': boston_roster}
    return render(request, 'nba-teams/celtics.html', context)

def brooklyn_roster(request):
    # Brooklyn Nets
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=BKN", headers=headers)
    res = conn.getresponse()
    data = res.read()
    brooklyn_roster = json.loads(data.decode("utf-8"))

    context = {'brooklyn_roster': brooklyn_roster}
    return render(request, 'nba-teams/nets.html', context)

def ny_roster(request):
    # NY Knicks
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=NYK", headers=headers)
    res = conn.getresponse()
    data = res.read()
    ny_roster = json.loads(data.decode("utf-8"))

    context = {'ny_roster': ny_roster}
    return render(request, 'nba-teams/knicks.html', context)

def philly_roster(request):
    # Philly 76ers
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=PHI", headers=headers)
    res = conn.getresponse()
    data = res.read()
    philly_roster = json.loads(data.decode("utf-8"))

    context = {'philly_roster': philly_roster}
    return render(request, 'nba-teams/sixers.html', context)

def toronto_roster(request):
    # Toronto Raptors
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=TOR", headers=headers)
    res = conn.getresponse()
    data = res.read()
    toronto_roster = json.loads(data.decode("utf-8"))

    context = {'toronto_roster': toronto_roster}
    return render(request, 'nba-teams/raptors.html', context)

def chicago_roster(request):
    # Chicago Bulls
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=CHI", headers=headers)
    res = conn.getresponse()
    data = res.read()
    chicago_roster = json.loads(data.decode("utf-8"))

    context = {'chicago_roster': chicago_roster}
    return render(request, 'nba-teams/bulls.html', context)

def cleveland_roster(request):
    # Cleveland Cavs
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=CLE", headers=headers)
    res = conn.getresponse()
    data = res.read()
    cleveland_roster = json.loads(data.decode("utf-8"))

    context = {'cleveland_roster': cleveland_roster}
    return render(request, 'nba-teams/cavs.html', context)

def detroit_roster(request):
    # detroit pistons
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=DET", headers=headers)
    res = conn.getresponse()
    data = res.read()
    detroit_roster = json.loads(data.decode("utf-8"))

    context = {'detroit_roster': detroit_roster}
    return render(request, 'nba-teams/pistons.html', context)

def milwaukee_roster(request):    
    # Milwaukee Bucks
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=MIL", headers=headers)
    res = conn.getresponse()
    data = res.read()
    milwaukee_roster = json.loads(data.decode("utf-8"))

    context = {'milwaukee_roster': milwaukee_roster}
    return render(request, 'nba-teams/bucks.html', context)

def indiana_roster(request):
    # Indiana Pacers
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=IND", headers=headers)
    res = conn.getresponse()
    data = res.read()
    indiana_roster = json.loads(data.decode("utf-8"))

    context = {'indiana_roster': indiana_roster}
    return render(request, 'nba-teams/pacers.html', context)

def atlanta_roster(request):
    # Atlanta Hawks
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=ATL", headers=headers)
    res = conn.getresponse()
    data = res.read()
    atlanta_roster = json.loads(data.decode("utf-8"))

    context = {'atlanta_roster': atlanta_roster}
    return render(request, 'nba-teams/hawks.html', context)

def charlotte_roster(request):
    # charlotte hornets
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=CHA", headers=headers)
    res = conn.getresponse()
    data = res.read()
    charlotte_roster = json.loads(data.decode("utf-8"))

    context = {'charlotte_roster': charlotte_roster}
    return render(request, 'nba-teams/hornets.html', context)

def miami_roster(request):
    # miami heat
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=MIA", headers=headers)
    res = conn.getresponse()
    data = res.read()
    miami_roster = json.loads(data.decode("utf-8"))

    context = {'miami_roster': miami_roster}
    return render(request, 'nba-teams/heat.html', context)

def orlando_roster(request):

    # orlando magic
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=ORL", headers=headers)
    res = conn.getresponse()
    data = res.read()
    orlando_roster = json.loads(data.decode("utf-8"))

    context = {'orlando_roster': orlando_roster}
    return render(request, 'nba-teams/magic.html', context)

def washington_roster(request):
    # washington wizards
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=WAS", headers=headers)
    res = conn.getresponse()
    data = res.read()
    washington_roster = json.loads(data.decode("utf-8"))

    context = {'washington_roster': washington_roster}
    return render(request, 'nba-teams/wizards.html', context)

    ##WEST##

def la_roster(request):
    # Los Angeles 
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=LAL", headers=headers)
    res = conn.getresponse()
    data = res.read()
    la_roster = json.loads(data.decode("utf-8"))

    context = {'la_roster': la_roster}
    return render(request, 'nba-teams/lakers.html', context)

def goldenstate_roster(request):
    # Golden State 
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=GS", headers=headers)
    res = conn.getresponse()
    data = res.read()
    goldenstate_roster = json.loads(data.decode("utf-8"))

    context = {'goldenstate_roster': goldenstate_roster}
    return render(request, 'nba-teams/warriors.html', context)

def sacramento_roster(request):
    # sacramento 
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=SAC", headers=headers)
    res = conn.getresponse()
    data = res.read()
    sacramento_roster = json.loads(data.decode("utf-8"))

    context = {'sacramento_roster': sacramento_roster}
    return render(request, 'nba-teams/kings.html', context)

def lac_roster(request):
    # lac 
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=LAC", headers=headers)
    res = conn.getresponse()
    data = res.read()
    lac_roster = json.loads(data.decode("utf-8"))

    context = {'lac_roster': lac_roster}
    return render(request, 'nba-teams/clippers.html', context)

def phoenix_roster(request):
    # phoenix 
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=PHO", headers=headers)
    res = conn.getresponse()
    data = res.read()
    phoenix_roster = json.loads(data.decode("utf-8"))

    context = {'phoenix_roster': phoenix_roster}
    return render(request, 'nba-teams/suns.html', context)

def denver_roster(request):
    # denver
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=DEN", headers=headers)
    res = conn.getresponse()
    data = res.read()
    denver_roster = json.loads(data.decode("utf-8"))

    context = {'denver_roster': denver_roster}
    return render(request, 'nba-teams/nuggets.html', context)

def minnesota_roster(request):
    #minnesota
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=MIN", headers=headers)
    res = conn.getresponse()
    data = res.read()
    minnesota_roster = json.loads(data.decode("utf-8"))

    context = {'minnesota_roster': minnesota_roster}
    return render(request, 'nba-teams/twolves.html', context)

def okc_roster(request):
    #okc
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=OKC", headers=headers)
    res = conn.getresponse()
    data = res.read()
    okc_roster = json.loads(data.decode("utf-8"))

    context = {'okc_roster': okc_roster}
    return render(request, 'nba-teams/thunder.html', context)

def portland_roster(request):
    #portland
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=POR", headers=headers)
    res = conn.getresponse()
    data = res.read()
    portland_roster = json.loads(data.decode("utf-8"))

    context = {'portland_roster': portland_roster}
    return render(request, 'nba-teams/blazers.html', context)

def utah_roster(request):
    #utah
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=UTA", headers=headers)
    res = conn.getresponse()
    data = res.read()
    utah_roster = json.loads(data.decode("utf-8"))

    context = {'utah_roster': utah_roster}
    return render(request, 'nba-teams/jazz.html', context)

def dallas_roster(request):
    #dallas
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=DAL", headers=headers)
    res = conn.getresponse()
    data = res.read()
    dallas_roster = json.loads(data.decode("utf-8"))

    context = {'dallas_roster': dallas_roster}
    return render(request, 'nba-teams/mavs.html', context)

def houston_roster(request):
    #houston
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=HOU", headers=headers)
    res = conn.getresponse()
    data = res.read()
    houston_roster = json.loads(data.decode("utf-8"))

    context = {'houston_roster': houston_roster}
    return render(request, 'nba-teams/rockets.html', context)

def memphis_roster(request):
    #memphis
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=MEM", headers=headers)
    res = conn.getresponse()
    data = res.read()
    memphis_roster = json.loads(data.decode("utf-8"))

    context = {'memphis_roster': memphis_roster}
    return render(request, 'nba-teams/grizz.html', context)

def san_roster(request):
    #san antonio
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=SA", headers=headers)
    res = conn.getresponse()
    data = res.read()
    san_roster = json.loads(data.decode("utf-8"))

    context = {'san_roster': san_roster}
    return render(request, 'nba-teams/spurs.html', context)

def neworleans_roster(request):
    #new orleans
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=NO", headers=headers)
    res = conn.getresponse()
    data = res.read()
    neworleans_roster = json.loads(data.decode("utf-8"))

    context = {'neworleans_roster': neworleans_roster}
    return render(request, 'nba-teams/pelicans.html', context)


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
