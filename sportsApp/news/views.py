from django.http import HttpResponse
import http.client, json
from django.shortcuts import render

# Create your views here.


def news(request):
    conn = http.client.HTTPSConnection("nba-latest-news.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21",
        'X-RapidAPI-Host': "nba-latest-news.p.rapidapi.com"
    }

    conn.request("GET", "/articles", headers=headers)

    res = conn.getresponse()
    data = res.read()

    news_data = json.loads(data.decode("utf-8"))

    context = {'news_data': news_data}

    return render(request, 'news.html', context)
