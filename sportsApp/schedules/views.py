from django.shortcuts import render
import http.client
import json
from django.shortcuts import render
import requests

# Create your views here.
def nba_teams(request):
    conn = http.client.HTTPSConnection("tank01-fantasy-stats.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "tank01-fantasy-stats.p.rapidapi.com"
    }
    conn.request("GET", "GET", "/getNBATeamSchedule?teamAbv=CHI", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))

    context = {'teams': data}
    return render(request, 'nbateams.html', context)