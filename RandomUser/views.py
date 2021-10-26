from django.shortcuts import render
from django.shortcuts import render
import requests


def index(request):
    r = requests.get('https://randomuser.me/api/')
    r = r.json()

    context = {
        "image": r['results'][0]['picture']['large'],
        "firstName": r['results'][0]['name']['first'],
        "lastName": r['results'][0]['name']['last'],
        "gender": r['results'][0]['gender'],
        "number": r['results'][0]['location']['street']['number'],
        "street": r['results'][0]['location']['street']['name'],
        "city": r['results'][0]['location']['city'],
        "state": r['results'][0]['location']['state']
    }

    return render(request, "User.html", context)
