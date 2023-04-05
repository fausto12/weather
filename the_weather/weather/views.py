from django.shortcuts import render
import requests


def index(request):
    API = 'bec728d68fa54dd3a813df9e47d550a3'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial'
    city = 'New york'

    res = requests.get(url.format(city, API)).json()

    city_weather = {
        'city': city,
        'temperature': res['main']['temp'],
        'description': res['weather'][0]['description'],
        'icon': res['weather'][0]['icon'],
    }
    context = {'city_weather': city_weather}

    return render(request, 'weather/index.html', context)
