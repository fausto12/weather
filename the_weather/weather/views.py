from django.shortcuts import render
import requests
from .models import City


def index(request):
    API = 'bec728d68fa54dd3a813df9e47d550a3'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial'
    city = 'New york'

    cities = City.objects.all()
    weather_data = []

    for city in cities:

        res = requests.get(url.format(city, API)).json()

        city_weather = {
            'city': city.name,
            'temperature': res['main']['temp'],
            'description': res['weather'][0]['description'],
            'icon': res['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data': weather_data}

    return render(request, 'weather/index.html', context)
