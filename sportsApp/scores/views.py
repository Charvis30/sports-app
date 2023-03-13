import requests
from django.http import JsonResponse

# Create your views here.

def live_score(request, team):
    url = ''
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)