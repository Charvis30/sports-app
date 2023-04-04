import requests
from django.shortcuts import render

    #Uses NewsAPI to get trending news
def trending(request):
    api_key = "6841fdab44ec405388ae6352ac4a9dfd"

    # NBA News
    nba_url = f"https://newsapi.org/v2/everything?q=basketball&apiKey={api_key}"
    nba_response = requests.get(nba_url)
    nba_news_data = nba_response.json()["articles"]

    # NFL News
    nfl_url = f"https://newsapi.org/v2/everything?q=american%20football&apiKey={api_key}"
    nfl_response = requests.get(nfl_url)
    nfl_news_data = nfl_response.json()["articles"]

    # Soccer News
    soccer_url = f"https://newsapi.org/v2/everything?q=soccer&apiKey={api_key}"
    soccer_response = requests.get(soccer_url)
    soccer_news_data = soccer_response.json()["articles"]

    # Combine the data from all APIs into a single dictionary
    context = {
        'nba_news_data': nba_news_data,
        'nfl_news_data': nfl_news_data,
        'soccer_news_data': soccer_news_data,
    }

    # Render the HTML template with the combined data
    return render(request, 'trending.html', context)
