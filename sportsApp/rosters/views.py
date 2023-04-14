import http.client
import json
from django.shortcuts import render

# Create your views here.

def nba_roster(request):

    # Boston
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=BOS", headers=headers)
    res = conn.getresponse()
    data = res.read()
    boston_roster = json.loads(data.decode("utf-8"))

    # Brooklyn
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=BKN", headers=headers)
    res = conn.getresponse()
    data = res.read()
    brooklyn_roster = json.loads(data.decode("utf-8"))

    # NY
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=NYK", headers=headers)
    res = conn.getresponse()
    data = res.read()
    ny_roster = json.loads(data.decode("utf-8"))


    # Philly
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=PHI", headers=headers)
    res = conn.getresponse()
    data = res.read()
    philly_roster = json.loads(data.decode("utf-8"))

    # Toronto
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=TOR", headers=headers)
    res = conn.getresponse()
    data = res.read()
    toronto_roster = json.loads(data.decode("utf-8"))

    # Chicagp
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=CHI", headers=headers)
    res = conn.getresponse()
    data = res.read()
    chicago_roster = json.loads(data.decode("utf-8"))

    # Cleveland
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=CLE", headers=headers)
    res = conn.getresponse()
    data = res.read()
    cleveland_roster = json.loads(data.decode("utf-8"))

    # detroit
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=DET", headers=headers)
    res = conn.getresponse()
    data = res.read()
    detroit_roster = json.loads(data.decode("utf-8"))
    
    # Milwaukee
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=MIL", headers=headers)
    res = conn.getresponse()
    data = res.read()
    milwaukee_roster = json.loads(data.decode("utf-8"))

    # Indiana
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=IND", headers=headers)
    res = conn.getresponse()
    data = res.read()
    indiana_roster = json.loads(data.decode("utf-8"))

    # Atlanta
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=ATL", headers=headers)
    res = conn.getresponse()
    data = res.read()
    atlanta_roster = json.loads(data.decode("utf-8"))

    # charlotte
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=CHA", headers=headers)
    res = conn.getresponse()
    data = res.read()
    charlotte_roster = json.loads(data.decode("utf-8"))

    # miami
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=MIA", headers=headers)
    res = conn.getresponse()
    data = res.read()
    miami_roster = json.loads(data.decode("utf-8"))

    # orlando
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=ORL", headers=headers)
    res = conn.getresponse()
    data = res.read()
    orlando_roster = json.loads(data.decode("utf-8"))

    # washington
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=WAS", headers=headers)
    res = conn.getresponse()
    data = res.read()
    washington_roster = json.loads(data.decode("utf-8"))

    ##WEST##

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

    # Golden State 
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "/getNBATeamRoster?teamAbv=GSW", headers=headers)
    res = conn.getresponse()
    data = res.read()
    goldenstate_roster = json.loads(data.decode("utf-8"))

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


    # Combine both contexts into one
    context = {

        # atlantic division
        'boston_roster': boston_roster,
        'brooklyn_roster': brooklyn_roster,
        'ny_roster': ny_roster,
        'philly_roster': philly_roster,
        'toronto_roster': toronto_roster,

        #central division
        'chicago_roster': chicago_roster,
        'cleveland_roster': cleveland_roster,
        'detroit_roster': detroit_roster,
        'milwaukee_roster': milwaukee_roster,
        'indiana_roster': indiana_roster,

        # southeast division
        'atlanta_roster': atlanta_roster,
        'charlotte_roster': charlotte_roster,
        'miami_roster': miami_roster,
        'orlando_roster': orlando_roster,
        'washington_roster': washington_roster,

        #pacific division
        'la_roster': la_roster,
        'goldenstate_roster': goldenstate_roster,
        'sacramento_roster': sacramento_roster,
        'lac_roster': lac_roster,
        'phoenix_roster': phoenix_roster,

        #northwest division
        'denver_roster': denver_roster,
        'minnesota_roster': minnesota_roster,
        'okc_roster': okc_roster,
        'portland_roster': portland_roster,
        'utah_roster': utah_roster,

        #southwest
        'dallas_roster': dallas_roster,
        'houston_roster': houston_roster,
        'san_roster': san_roster,
        'memphis_roster': memphis_roster,
        'neworleans_roster': neworleans_roster,

    }
    
    return render(request, 'baseball.html', context)