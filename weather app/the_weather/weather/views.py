import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=67b2248e9c90b626cee6d5a6d436f22a'
    city = 'Las Vegas'
    r = requests.get(url.format(city)).json()
    city_weather = {
        'city' : city,
        'temprature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' :  r['weather'][0]['icon'],
    }
    context = {'city_weather': city_weather}
    return render(request,'weather/weather.html')