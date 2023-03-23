from django.http import HttpResponse
import http.client

def basketball_data(request):
    conn = http.client.HTTPSConnection("livescore6.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "livescore6.p.rapidapi.com",
        'x-rapidapi-key': "62179425a4mshc82870dfbd61b7cp115211jsne5fa10ef3b21"
        }
    conn.request("GET", "/leagues/v2/list?Category=basketball", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return HttpResponse(data.decode("utf-8"))
