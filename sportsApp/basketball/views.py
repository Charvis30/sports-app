from django.http import HttpResponse
import http.client
from django.shortcuts import render


def basketball_data(request):
    conn = http.client.HTTPSConnection("livescore6.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "livescore6.p.rapidapi.com",
        'x-rapidapi-key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21"
        }
    conn.request("GET", "/matches/v2/list-by-league?Category=basketball&Ccd=nba", headers=headers)
    res = conn.getresponse()
    data = res.read()
    context = {'api_data': data.decode("utf-8")}
    return render(request, 'basketball.html', context)