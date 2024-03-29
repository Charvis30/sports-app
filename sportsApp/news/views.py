import http.client
import json
from django.shortcuts import render

def news(request):
    # NBA API
    nba_conn = http.client.HTTPSConnection("nba-latest-news.p.rapidapi.com")
    nba_headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "nba-latest-news.p.rapidapi.com"
    }
    nba_conn.request("GET", "/articles", headers=nba_headers)
    nba_res = nba_conn.getresponse()
    nba_data = nba_res.read()
    nba_news_data = json.loads(nba_data.decode("utf-8"))

    

    # Combine the data from all APIs into a single dictionary
    context = {
        'nba_news_data': nba_news_data,
        

    }

    # Render the HTML template with the combined data
    return render(request, 'news.html', context)